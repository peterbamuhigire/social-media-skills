from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_package_integrity as package_check


def fixture(root: Path) -> None:
    skill = root / "skills" / "category" / "example"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("example\n", encoding="utf-8")
    plugin_dir = root / ".claude-plugin"
    plugin_dir.mkdir()
    (plugin_dir / "plugin.json").write_text(json.dumps({
        "name": "example", "version": "1.0.0", "skills": ["./skills/category/example/"]
    }), encoding="utf-8")
    (plugin_dir / "marketplace.json").write_text(json.dumps({
        "name": "catalogue", "plugins": [{"name": "example", "version": "1.0.0", "source": "./"}]
    }), encoding="utf-8")


class PackageIntegrityTests(unittest.TestCase):
    def test_manifest_identity_and_skill_paths_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            self.assertEqual([], package_check.validate_manifests(root))

    def test_rejects_manifest_identity_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            market = root / ".claude-plugin" / "marketplace.json"
            payload = json.loads(market.read_text(encoding="utf-8"))
            payload["plugins"][0]["name"] = "other"
            market.write_text(json.dumps(payload), encoding="utf-8")
            self.assertIn("marketplace plugin name differs from plugin manifest",
                          package_check.validate_manifests(root))

    def test_rejects_manifest_skill_path_set_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            plugin_path = root / ".claude-plugin" / "plugin.json"
            payload = json.loads(plugin_path.read_text(encoding="utf-8"))
            payload["skills"] = []
            plugin_path.write_text(json.dumps(payload), encoding="utf-8")
            self.assertTrue(any("declared skill paths differ from filesystem" in error
                                for error in package_check.validate_manifests(root)))

    def test_rejects_symlinked_skill_file(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as external:
            root = Path(tmp)
            fixture(root)
            skill_file = root / "skills" / "category" / "example" / "SKILL.md"
            skill_file.unlink()
            target = Path(external) / "SKILL.md"
            target.write_text("external\n", encoding="utf-8")
            try:
                skill_file.symlink_to(target)
            except OSError as exc:
                self.skipTest(f"symlink creation unavailable: {exc}")
            self.assertTrue(any("skill path contains a symlink" in error
                                for error in package_check.validate_manifests(root)))

    def test_rejects_symlinked_skill_directory(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as external:
            root = Path(tmp)
            fixture(root)
            skill_dir = root / "skills" / "category" / "example"
            skill_dir.rename(Path(external) / "example")
            try:
                skill_dir.symlink_to(Path(external) / "example", target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"symlink creation unavailable: {exc}")
            self.assertTrue(any("skill path contains a symlink" in error
                                for error in package_check.validate_manifests(root)))

    def test_counts_symlink_entries_without_following_directory_links(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as external:
            root = Path(tmp)
            (root / "inside").mkdir()
            (root / "inside" / "file").write_text("x", encoding="utf-8")
            (Path(external) / "outside").write_text("x", encoding="utf-8")
            try:
                (root / "linked-dir").symlink_to(external, target_is_directory=True)
                (root / "linked-file").symlink_to(Path(external) / "outside")
            except OSError as exc:
                self.skipTest(f"symlink creation unavailable: {exc}")
            self.assertEqual(3, package_check.count_entries(root))

    def test_unreadable_inventory_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            def fake_walk(root, *, followlinks, onerror):
                onerror(PermissionError("fixture unreadable subtree"))
                yield str(root), [], []

            with patch.object(package_check.os, "walk", side_effect=fake_walk):
                with self.assertRaisesRegex(PermissionError, "fixture unreadable subtree"):
                    package_check.count_entries(Path(tmp))

    def test_hard_ceiling_boundary_for_checkout_and_package(self):
        self.assertEqual([], package_check.capacity_findings(5000, 5000))
        self.assertEqual(["checkout file entries 5001 exceed hard limit 5000"],
                         package_check.capacity_findings(5001, 5000))
        self.assertEqual(["package file entries 5001 exceed hard limit 5000"],
                         package_check.capacity_findings(5000, 5001))

    def test_counts_5000_and_5001_real_file_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for index in range(5000):
                (root / f"file-{index:04d}").touch()
            self.assertEqual(5000, package_check.count_entries(root))
            self.assertEqual([], package_check.capacity_findings(
                package_check.count_entries(root), package_check.count_entries(root, package=True)))
            (root / "file-5000").touch()
            count = package_check.count_entries(root)
            self.assertEqual(5001, count)
            self.assertIn("checkout file entries 5001 exceed hard limit 5000",
                          package_check.capacity_findings(count, 5000))

    def test_audit_enforces_lower_fixture_limit_and_rejects_higher_override(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture(root)
            errors, _ = package_check.audit_repository(root, limit=2)
            self.assertTrue(any("exceed hard limit 2" in error for error in errors))
            with self.assertRaises(ValueError):
                package_check.audit_repository(root, limit=5001)


if __name__ == "__main__":
    unittest.main()
