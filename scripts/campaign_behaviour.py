#!/usr/bin/env python3
"""Run a deterministic, fictional campaign handoff fixture.

Known release-gate defects return ``BLOCKED`` with a stage and reason; malformed
fixture structure without a recognised gate reason returns ``FAIL``.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


STAGES = ("brief", "calendar", "approval", "evidence", "report")
APPROVAL_STATUSES = {"approved", "blocked"}
REPORT_DECISIONS = {"continue", "stop", "reallocate", "revise", "iterate", "learn", "hold"}


def _missing(value: Any) -> bool:
    return value is None or value == "" or value == []


def _block_stage(stage_results: dict[str, str], blocking_reasons: list[str], stage: str, reason: str | None = None) -> None:
    stage_results[stage] = "blocked"
    if reason and reason not in blocking_reasons:
        blocking_reasons.append(reason)


def evaluate_case(case: dict[str, Any]) -> dict[str, Any]:
    """Validate one fixture case without contacting a platform or mutating state."""

    issues: list[str] = []
    blocking_reasons: list[str] = []
    stage_results = {stage: "pass" for stage in STAGES}

    def issue(message: str, stage: str | None = None, reason: str | None = None) -> None:
        issues.append(message)
        if stage:
            _block_stage(stage_results, blocking_reasons, stage, reason)

    if case.get("stage_order") != list(STAGES):
        issues.append("stage_order must be brief -> calendar -> approval -> evidence -> report")

    brief = case.get("brief")
    calendar = case.get("calendar")
    approval = case.get("approval")
    evidence = case.get("evidence")
    report = case.get("report")
    campaign_id = brief.get("campaign_id") if isinstance(brief, dict) else None
    for stage, value in (("brief", brief), ("calendar", calendar), ("approval", approval), ("evidence", evidence), ("report", report)):
        if not isinstance(value, dict):
            issue(f"{stage} stage is missing or is not an object", stage, "missing-stage")

    if isinstance(brief, dict):
        for field in ("brief_id", "campaign_id", "objective", "audience", "platforms", "approval_owner", "approval_boundary"):
            if _missing(brief.get(field)):
                issue(f"brief.{field} is required", "brief", "incomplete-brief")

    entry_ids: list[str] = []
    if isinstance(calendar, dict):
        if calendar.get("campaign_id") != campaign_id:
            issue("calendar.campaign_id does not match brief.campaign_id", "calendar", "calendar-campaign-mismatch")
        entries = calendar.get("entries")
        if not isinstance(entries, list) or not entries:
            issue("calendar.entries must contain at least one entry", "calendar", "calendar-integrity")
        else:
            for entry in entries:
                if not isinstance(entry, dict):
                    issue("calendar entry is not an object", "calendar", "calendar-integrity")
                    continue
                entry_id = entry.get("entry_id")
                if _missing(entry_id) or entry_id in entry_ids:
                    issue("calendar entries require unique entry_id values", "calendar", "calendar-integrity")
                else:
                    entry_ids.append(entry_id)
                for field in ("brief_id", "date", "platform", "owner", "status"):
                    if _missing(entry.get(field)):
                        issue(f"calendar entry {entry_id or '<missing>'}.{field} is required", "calendar", "calendar-integrity")
                if isinstance(brief, dict) and entry.get("brief_id") != brief.get("brief_id"):
                    issue(f"calendar entry {entry_id or '<missing>'} does not trace to brief.brief_id", "calendar", "calendar-brief-mismatch")

    approval_status = None
    if isinstance(approval, dict):
        approval_status = approval.get("status")
        if approval.get("campaign_id") != campaign_id:
            issue("approval.campaign_id does not match brief.campaign_id", "approval", "approval-campaign-mismatch")
        if approval_status not in APPROVAL_STATUSES:
            issue("approval.status must be approved or blocked", "approval", "approval-status-invalid")
        elif approval_status == "approved":
            if _missing(approval.get("approval_id")) or _missing(approval.get("approval_evidence_id")):
                issue("approved campaign requires approval_id and approval_evidence_id", "approval", "missing-approval-evidence")
            if approval.get("approved_entry_ids") != entry_ids:
                issue("approved_entry_ids must exactly match calendar entry IDs", "approval", "approval-calendar-mismatch")
        else:
            omissions = approval.get("missing")
            if not isinstance(omissions, list) or not omissions:
                issue("blocked approval must name at least one omission", "approval", "blocked-approval-contract")
            _block_stage(stage_results, blocking_reasons, "approval", "approval-not-approved")

    source_ids: set[str] = set()
    if isinstance(evidence, dict):
        if evidence.get("campaign_id") != campaign_id:
            issue("evidence.campaign_id does not match brief.campaign_id", "evidence", "evidence-campaign-mismatch")
        sources = evidence.get("source_records")
        if not isinstance(sources, list) or not sources:
            issue("evidence.source_records must contain at least one labelled source", "evidence", "missing-evidence")
        else:
            for source in sources:
                if not isinstance(source, dict) or _missing(source.get("id")) or _missing(source.get("label")):
                    issue("each evidence source requires an id and label", "evidence", "missing-evidence")
                elif source["id"] in source_ids:
                    issue(f"duplicate evidence source id: {source['id']}", "evidence", "evidence-lineage-mismatch")
                else:
                    source_ids.add(source["id"])
        metrics = evidence.get("metrics")
        if not isinstance(metrics, list) or not metrics:
            issue("evidence.metrics must contain at least one metric row", "evidence", "missing-evidence")
        else:
            for metric in metrics:
                if not isinstance(metric, dict) or _missing(metric.get("name")) or _missing(metric.get("source_id")):
                    issue("each metric requires a name and source_id", "evidence", "evidence-lineage-mismatch")
                elif source_ids and metric["source_id"] not in source_ids:
                    issue(f"metric {metric['name']} cites an unknown evidence source", "evidence", "evidence-lineage-mismatch")

    if isinstance(report, dict):
        if report.get("campaign_id") != campaign_id:
            issue("report.campaign_id does not match brief.campaign_id", "report", "report-campaign-mismatch")
        if report.get("decision") not in REPORT_DECISIONS:
            issue("report.decision is not a recognised decision", "report", "invalid-report-decision")
        evidence_ids = report.get("evidence_ids")
        if stage_results["evidence"] != "blocked" and evidence_ids and not set(evidence_ids).issubset(source_ids):
            issue("report.evidence_ids must point to evidence source records", "report", "report-evidence-inconsistency")

        if report.get("calendar_entry_ids") != entry_ids:
            issue("report.calendar_entry_ids must exactly match calendar entry IDs", "report", "report-calendar-inconsistency")

        upstream_blocked = any(stage_results[stage] == "blocked" for stage in ("brief", "calendar", "approval", "evidence"))
        if approval_status == "approved" and not upstream_blocked:
            metrics = evidence.get("metrics") if isinstance(evidence, dict) else None
            expected_metrics = {
                (metric.get("name"), metric.get("source_id"))
                for metric in metrics
                if isinstance(metric, dict) and not _missing(metric.get("name")) and not _missing(metric.get("source_id"))
            }
            actual_rows = report.get("metric_rows")
            actual_metrics = {
                (row.get("name"), row.get("evidence_id"))
                for row in actual_rows
                if isinstance(row, dict) and not _missing(row.get("name")) and not _missing(row.get("evidence_id"))
            } if isinstance(actual_rows, list) else set()
            if actual_metrics != expected_metrics:
                issue("report.metric_rows must reconcile evidence metrics", "report", "report-evidence-inconsistency")

            if report.get("workflow_status") != "complete" or report.get("publish_authority") is not False:
                issue("approved fixture must be complete while retaining false live-publish authority", "report")
            if report.get("not_assessed"):
                issue("approved fixture must not hide an unresolved workflow omission", "report")
        elif approval_status == "approved":
            if report.get("workflow_status") != "blocked" or report.get("publish_authority") is not False:
                issue("report must remain blocked when an upstream approval, calendar or evidence gate is blocked", "report")
            if not isinstance(report.get("not_assessed"), list) or not report.get("not_assessed"):
                issue("blocked report must name the unresolved upstream gate", "report")
        elif approval_status == "blocked":
            omissions = report.get("blocked_omissions")
            not_assessed = report.get("not_assessed")
            if report.get("workflow_status") != "blocked" or report.get("publish_authority") is not False:
                issue("blocked fixture must remain blocked and retain false live-publish authority", "report")
            if not isinstance(omissions, list) or not omissions:
                issue("blocked report must name the omitted approval evidence", "report")
            if not isinstance(not_assessed, list) or not any("approval" in item.lower() for item in not_assessed):
                issue("blocked report must mark approval as not assessed", "report")
            stage_results["evidence"] = "not assessed"
            stage_results["report"] = "blocked"

    verdict = "BLOCKED" if blocking_reasons else ("FAIL" if issues else "PASS")
    expected = case.get("expected_verdict")
    fixture_match = verdict == expected
    if not fixture_match:
        issues.append(f"expected_verdict={expected!r} but observed {verdict!r}")

    return {
        "id": case.get("id", "<missing>"),
        "verdict": verdict,
        "expected_verdict": expected,
        "fixture_match": fixture_match,
        "stage_results": stage_results,
        "blocking_reasons": blocking_reasons,
        "issues": issues,
    }


def run_fixture(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not data.get("fixture_label", "").startswith("FICTIONAL TEST DATA"):
        raise ValueError("fixture must be explicitly labelled fictional test data")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("fixture must contain at least one case")
    return [evaluate_case(case) for case in cases]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "fixture",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "campaign-behaviour.json",
    )
    args = parser.parse_args()
    results = run_fixture(args.fixture)
    passed = sum(result["fixture_match"] and result["verdict"] == "PASS" for result in results)
    blocked = sum(result["fixture_match"] and result["verdict"] == "BLOCKED" for result in results)
    failed = len(results) - passed - blocked
    print(f"campaign fixture cases={len(results)} pass={passed} blocked={blocked} fail={failed}")
    for result in results:
        print(f"{result['id']}: {result['verdict']} stages={result['stage_results']}")
        for issue in result["issues"]:
            label = "BLOCK" if result["verdict"] == "BLOCKED" else "FAIL"
            print(f"  {label} {issue}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
