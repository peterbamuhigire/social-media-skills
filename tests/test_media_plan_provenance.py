import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_media_plan_provenance.py"
spec = importlib.util.spec_from_file_location("media_provenance", SCRIPT)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def valid_row():
    return {"channel": "Example", **{
        key: {"value": value, "origin": "synthetic_assumption", "source": "fixture assumption"}
        for key, value in (("budget_ugx", 1000), ("cpm_ugx", 25), ("frequency", 2))
    }}


class MediaPlanProvenanceTests(unittest.TestCase):
    def test_valid_numeric_origins_and_sources_pass(self):
        self.assertEqual(module.validate_rows([valid_row()]), [])

    def test_missing_origin_fails(self):
        row = valid_row()
        del row["budget_ugx"]["origin"]
        self.assertTrue(any("budget_ugx.origin" in item for item in module.validate_rows([row])))

    def test_unknown_origin_fails(self):
        row = valid_row()
        row["cpm_ugx"]["origin"] = "estimated"
        self.assertTrue(any("cpm_ugx.origin" in item for item in module.validate_rows([row])))

    def test_missing_source_fails(self):
        row = valid_row()
        row["frequency"]["source"] = "  "
        self.assertTrue(any("frequency.source" in item for item in module.validate_rows([row])))

    def test_zero_or_nonfinite_frequency_fails(self):
        for value in (0, float("inf")):
            with self.subTest(value=value):
                row = valid_row()
                row["frequency"]["value"] = value
                self.assertTrue(any("frequency.value" in item for item in module.validate_rows([row])))

    def test_invalid_json_input_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "invalid.json"
            path.write_text(json.dumps({"rows": [valid_row() | {"budget_ugx": 1000}]}), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL", result.stdout)


if __name__ == "__main__":
    unittest.main()
