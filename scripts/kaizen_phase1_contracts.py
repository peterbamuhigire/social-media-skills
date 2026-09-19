#!/usr/bin/env python3
"""Validate the bounded Phase 1 social-content contracts with synthetic data."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SUPPORT_STATES = {"supported", "unsupported", "synthesis", "inference", "no-source"}
RIGHTS_STATES = {"cleared", "owned", "licensed", "permission-pending", "denied", "not-applicable"}


def _missing(value: Any) -> bool:
    return value is None or value == "" or value == []


def _result(case_id: str, verdict: str, issues: list[str], unassessed: list[str]) -> dict[str, Any]:
    return {"id": case_id, "verdict": verdict, "issues": issues, "not_assessed": unassessed}


def validate_content_unit(case: dict[str, Any]) -> dict[str, Any]:
    """Check a reader-first unit without contacting a platform or mutating state."""

    issues: list[str] = []
    unassessed: list[str] = []
    required = ("brief_id", "reader", "objective", "channel", "destination", "claims", "rights", "review")
    for field in required:
        if _missing(case.get(field)):
            issues.append(f"{field} is required")

    reader = case.get("reader")
    if isinstance(reader, dict):
        for field in ("audience", "reader_job", "utility", "inspiration", "empathy"):
            if _missing(reader.get(field)):
                issues.append(f"reader.{field} is required")
    else:
        issues.append("reader must be an object")

    claims = case.get("claims")
    if isinstance(claims, list):
        for claim in claims:
            if not isinstance(claim, dict):
                issues.append("each claim must be an object")
                continue
            for field in ("claim_id", "text", "source_scope", "source_ids", "publication_date", "accessed_on", "support_review"):
                if _missing(claim.get(field)):
                    issues.append(f"claim.{field} is required")
            review = claim.get("support_review")
            if isinstance(review, dict):
                state = review.get("state")
                if state not in SUPPORT_STATES:
                    issues.append("claim.support_review.state is invalid")
                source_ids = claim.get("source_ids")
                if not isinstance(source_ids, list):
                    issues.append("claim.source_ids must be a list")
                elif state == "no-source" and source_ids:
                    issues.append("no-source claim must use an empty source_ids list")
                elif state != "no-source" and not source_ids:
                    issues.append("claim requires at least one source id")
                if state in {"unsupported", "no-source"}:
                    issues.append(f"claim {claim.get('claim_id', '<missing>')} is unresolved")
                elif state == "inference":
                    unassessed.append(f"claim {claim.get('claim_id', '<missing>')} is an inference")
            else:
                issues.append("claim.support_review must be an object")

    rights = case.get("rights")
    if isinstance(rights, list):
        for asset in rights:
            if not isinstance(asset, dict):
                issues.append("each rights row must be an object")
                continue
            for field in ("asset_id", "asset_type", "rights_status", "rights_owner", "reviewed_on"):
                if _missing(asset.get(field)):
                    issues.append(f"rights.{field} is required")
            status = asset.get("rights_status")
            if status not in RIGHTS_STATES:
                issues.append(f"rights status is invalid for {asset.get('asset_id', '<missing>')}")
            elif status in {"permission-pending", "denied"}:
                issues.append(f"rights for {asset.get('asset_id', '<missing>')} are not cleared")

    destination = case.get("destination")
    cta = case.get("cta")
    if isinstance(destination, dict) and isinstance(cta, dict):
        kind = destination.get("kind")
        if kind not in {"website", "whatsapp", "form", "profile", "none"}:
            issues.append("destination.kind is invalid")
        if _missing(destination.get("promise")):
            issues.append("destination.promise is required")
        if kind != "none" and _missing(destination.get("url")):
            issues.append("destination.url is required for a click destination")
        if destination.get("status") != "verified" and kind != "none":
            unassessed.append("destination verification")
        if cta.get("destination_kind") != kind or cta.get("destination_url") != destination.get("url"):
            issues.append("CTA destination does not match the canonical destination")
        if _missing(cta.get("action")):
            issues.append("cta.action is required")
    else:
        issues.append("destination and cta are required objects")
        unassessed.append("destination review")

    review = case.get("review")
    if isinstance(review, dict):
        for field in ("owner", "reviewer", "reviewed_on", "language_review"):
            if _missing(review.get(field)):
                unassessed.append(f"review.{field}")
        if review.get("language_review") != "completed":
            unassessed.append("language review")
    else:
        unassessed.append("human review")

    verdict = "BLOCKED" if issues else ("NOT_ASSESSED" if unassessed else "PASS")
    return _result(case.get("id", "<missing>"), verdict, issues, sorted(set(unassessed)))


def validate_identity(case: dict[str, Any]) -> dict[str, Any]:
    identity = case.get("identity")
    issues: list[str] = []
    unassessed: list[str] = []
    if not isinstance(identity, dict):
        return _result(case.get("id", "<missing>"), "BLOCKED", ["identity must be an object"], [])
    for field in ("display_name", "locale"):
        if _missing(identity.get(field)):
            issues.append(f"identity.{field} is required")
    allowed = {"display_name", "locale", "legal_name", "preferred_name", "pronunciation", "script", "relationship"}
    for field in set(identity) - allowed:
        issues.append(f"identity field {field} is not recognised")
    if not case.get("needs_legal_name", False) and any(key in identity for key in ("legal_name", "preferred_name")):
        issues.append("legal/preferred identity field is unnecessary for this purpose")
    if not case.get("needs_pronunciation", False) and any(key in identity for key in ("pronunciation", "script")):
        issues.append("pronunciation/script field is unnecessary for this purpose")
    if case.get("needs_legal_name") and not identity.get("legal_name"):
        issues.append("legal_name is required for the stated purpose")
    if case.get("needs_pronunciation") and not identity.get("pronunciation"):
        issues.append("pronunciation is required for the stated purpose")
    native_review = case.get("native_review")
    if not isinstance(native_review, dict) or native_review.get("status") != "completed":
        unassessed.append("native-language review")
    elif _missing(native_review.get("reviewer")) or _missing(native_review.get("reviewed_on")):
        unassessed.append("native-language review evidence")
    verdict = "BLOCKED" if issues else ("NOT_ASSESSED" if unassessed else "PASS")
    return _result(case.get("id", "<missing>"), verdict, issues, sorted(set(unassessed)))


def validate_experiment(case: dict[str, Any]) -> dict[str, Any]:
    required = ("experiment_id", "source_scope", "source_ids", "hypothesis", "sample", "privacy_boundary", "action", "primary_outcome", "counter_metric", "guardrail", "test_window", "decision_rule", "owner", "review_date", "knowledge_record")
    issues: list[str] = []
    unassessed: list[str] = []
    for field in required:
        if _missing(case.get(field)):
            unassessed.append(field)
    sample = case.get("sample")
    denominator = sample.get("denominator") if isinstance(sample, dict) else None
    if not isinstance(denominator, int) or denominator <= 0:
        unassessed.append("sample denominator")
    knowledge = case.get("knowledge_record")
    if isinstance(knowledge, dict):
        if not isinstance(knowledge.get("source_ids"), list) or not knowledge.get("source_ids"):
            unassessed.append("knowledge source link")
        elif not set(case.get("source_ids", [])).issubset(set(knowledge["source_ids"])):
            issues.append("knowledge record does not link to original evidence")
    else:
        unassessed.append("knowledge record")
    verdict = "BLOCKED" if issues else ("NOT_ASSESSED" if unassessed else "PASS")
    return _result(case.get("id", "<missing>"), verdict, issues, sorted(set(unassessed)))


def run_fixture(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not data.get("fixture_label", "").startswith("FICTIONAL TEST DATA"):
        raise ValueError("fixture must be explicitly labelled fictional test data")
    results: list[dict[str, Any]] = []
    for case in data.get("content_units", []):
        result = validate_content_unit(case)
        result["expected_verdict"] = case.get("expected_verdict")
        result["fixture_match"] = result["verdict"] == result["expected_verdict"]
        results.append(result)
    for case in data.get("identities", []):
        result = validate_identity(case)
        result["expected_verdict"] = case.get("expected_verdict")
        result["fixture_match"] = result["verdict"] == result["expected_verdict"]
        results.append(result)
    for case in data.get("experiments", []):
        result = validate_experiment(case)
        result["expected_verdict"] = case.get("expected_verdict")
        result["fixture_match"] = result["verdict"] == result["expected_verdict"]
        results.append(result)
    if not results:
        raise ValueError("fixture has no cases")
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=ROOT / "tests" / "fixtures" / "kaizen-phase1-contracts.json")
    args = parser.parse_args()
    results = run_fixture(args.fixture)
    failures = [result for result in results if not result["fixture_match"]]
    counts = {verdict: sum(result["verdict"] == verdict for result in results) for verdict in ("PASS", "BLOCKED", "NOT_ASSESSED")}
    print(f"kaizen phase1 cases={len(results)} pass={counts['PASS']} blocked={counts['BLOCKED']} not_assessed={counts['NOT_ASSESSED']} fail={len(failures)}")
    for result in results:
        print(f"{result['id']}: {result['verdict']} issues={len(result['issues'])} not_assessed={result['not_assessed']}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
