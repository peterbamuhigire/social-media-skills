#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
START_MARKER = "<!-- dual-compat:start -->"
END_MARKER = "<!-- dual-compat:end -->"


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"(?s)\A(---\n.*?\n---\n)(.*)\Z", text)
    if not match:
        raise ValueError("Missing YAML frontmatter")
    return match.group(1), match.group(2)


def clean_whitespace(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip("\n") + "\n"


def remove_existing_block(body: str) -> str:
    pattern = re.compile(
        rf"\n?{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}\n?",
        re.S,
    )
    return re.sub(pattern, "\n\n", body)


def category_for(skill_name: str) -> str:
    if skill_name.startswith("deck-"):
        return "deck"
    if skill_name.startswith("meta-"):
        return "analysis"
    if skill_name.startswith("playbook-"):
        return "playbook"
    if skill_name.startswith("platform-"):
        return "platform"
    if skill_name.startswith("policy-"):
        return "policy"
    if skill_name.startswith("training-"):
        return "training"
    if skill_name.startswith("biz-dev-"):
        return "business-development"
    if re.match(r"^\d\d-", skill_name):
        return "numbered"
    if skill_name.startswith("strategy-") or skill_name in {
        "peso-integrated-strategy",
        "owned-media-strategy",
        "social-commerce-strategy",
    }:
        return "strategy"
    if skill_name.startswith("ai-") or skill_name.startswith("brand-voice-") or skill_name.startswith("prompt-"):
        return "ai"
    if skill_name in {"east-african-english", "language-standards", "content-writing"}:
        return "standards"
    if skill_name in {"skill-writing", "skill-safety-audit"}:
        return "meta-skill"
    if any(
        token in skill_name
        for token in [
            "writer",
            "copywriter",
            "caption",
            "hashtag",
            "content-ideas",
            "whitepaper",
            "brochure",
            "direct-mail",
            "blog-idea",
        ]
    ):
        return "content"
    if skill_name.startswith("framework-"):
        return "framework"
    return "general"


def use_when_lines(description: str, category: str) -> list[str]:
    lines = [f"- {description.rstrip('.')}."]
    if category in {"deck", "analysis", "playbook", "platform", "policy", "training", "business-development", "numbered", "strategy", "ai", "content", "framework"}:
        lines.append("- Use this skill when it is the closest match to the requested deliverable or workflow.")
    elif category == "standards":
        lines.append("- Apply it alongside the primary deliverable skill whenever wording, tone, or editorial quality needs control.")
    elif category == "meta-skill":
        lines.append("- Use it when maintaining, reviewing, or extending the skill repository itself.")
    return lines


def do_not_use_lines(category: str) -> list[str]:
    shared = [
        "- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.",
        "- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.",
    ]
    if category == "standards":
        return shared + [
            "- Do not use this skill as a substitute for the main document, strategy, or copy-generation skill.",
        ]
    if category == "meta-skill":
        return shared + [
            "- Do not invoke this skill for client deliverables; it is for repository maintenance and governance.",
        ]
    return shared


def workflow_lines(skill_name: str, body: str, category: str) -> list[str]:
    lines = []
    if re.search(r"^##\s+Required Input", body, re.M):
        lines.append("1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.")
    else:
        lines.append("1. Confirm the objective, audience, and context needed to run this skill well.")
    lines.append("2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.")
    if (ROOT / skill_name / "references").exists():
        lines.append("3. Read files in `references/` only when the body points to them or when you need the deeper framework, examples, or evidence.")
        lines.append("4. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.")
    else:
        lines.append("3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.")
    if category == "standards":
        lines = [
            "1. Read the requested draft, source text, or surrounding brief before making language decisions.",
            "2. Apply the rules in this skill consistently across the whole deliverable, not only the obvious problem lines.",
            "3. Return corrected copy, guidance, or a style-constrained draft that the paired skill can use directly.",
        ]
    if category == "meta-skill":
        lines = [
            "1. Inspect the target skill, file set, or repository area in full before making recommendations.",
            "2. Apply the repository rules and any checks defined in this skill step by step.",
            "3. Return a clear verdict, concrete findings, and the next actions required.",
        ]
    return lines


def output_lines(category: str, skill_name: str) -> list[str]:
    if category == "deck":
        return ["- A slide-by-slide markdown deck using `Headline`, `Bullets`, `Speaker Notes`, and `Visual Direction` for every slide."]
    if category in {"playbook", "platform", "policy", "training", "strategy", "business-development", "framework"}:
        return ["- A structured markdown document, plan, playbook, or strategy ready for client-facing or internal use."]
    if category == "analysis":
        return ["- A structured audit, report, model, or analytical framework in markdown, with decisions and recommendations tied to evidence."]
    if category == "content":
        return ["- The requested copy asset or idea set in markdown, written to publish, review, or adapt without major rework."]
    if category == "standards":
        return ["- A reusable style standard, rewrite, or editing pass that improves another deliverable rather than replacing it."]
    if category == "meta-skill":
        return ["- A repository maintenance output such as a review, audit, packaging step, or skill-authoring recommendation."]
    if category == "numbered":
        return ["- A structured onboarding, strategy, or planning document in markdown, ready to hand off to the next skill in the workflow."]
    if category == "ai":
        return ["- An AI-focused strategy, audit, system design, or prompt asset in markdown with human review and control points."]
    return ["- The primary deliverable requested by this skill, structured in markdown and ready for immediate use."]


def anti_pattern_lines(category: str) -> list[str]:
    lines = [
        "- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.",
        "- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.",
    ]
    if category == "deck":
        lines.append("- Do not turn the deck into a generic outline; every slide needs an assertion, usable speaker notes, and visual direction.")
    elif category == "standards":
        lines.append("- Do not mix British and American English, and do not apply the rules inconsistently across the same deliverable.")
    elif category == "meta-skill":
        lines.append("- Do not approve unclear or risky repository changes without stating the exact issue and the action required.")
    else:
        lines.append("- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.")
    return lines


def reference_lines(skill_dir: Path) -> list[str]:
    refs_dir = skill_dir / "references"
    if not refs_dir.exists():
        return ["- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused."]
    files = sorted(p.name for p in refs_dir.iterdir() if p.is_file())
    if not files:
        return ["- `references/` exists but is currently empty; keep detailed frameworks, examples, and supporting material there as the skill grows."]
    return [f"- Read `references/{name}` when you need the deeper framework, examples, or supporting material it contains." for name in files]


def build_block(skill_name: str, description: str, body: str) -> str:
    category = category_for(skill_name)
    sections = [
        ("Use when", use_when_lines(description, category)),
        ("Do not use when", do_not_use_lines(category)),
        ("Workflow", workflow_lines(skill_name, body, category)),
        ("Anti-Patterns", anti_pattern_lines(category)),
        ("Outputs", output_lines(category, skill_name)),
        ("References", reference_lines(ROOT / skill_name)),
    ]
    parts = [START_MARKER]
    for heading, lines in sections:
        parts.append(f"## {heading}")
        parts.extend(lines)
        parts.append("")
    parts.append(END_MARKER)
    return "\n".join(parts).strip() + "\n"


def extract_description(frontmatter: str) -> str:
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("description:"):
            continue
        value = line.split(":", 1)[1].strip()
        if value in {">", "|"}:
            chunks = []
            for follow in lines[index + 1 :]:
                if not follow.startswith("  "):
                    break
                chunks.append(follow.strip())
            description = " ".join(chunks).strip()
            if description:
                return description
        if value:
            return value
    raise ValueError("Frontmatter missing description")


def insert_block(body: str, block: str) -> str:
    body = remove_existing_block(body)
    h1_match = re.match(r"(?s)\A(# .+?\n)(.*)\Z", body.strip("\n"))
    if not h1_match:
        return clean_whitespace(block + "\n" + body)

    title = h1_match.group(1)
    remainder = h1_match.group(2).lstrip("\n")
    first_h2 = re.search(r"^##\s+", remainder, re.M)
    if first_h2:
        intro = remainder[: first_h2.start()].rstrip()
        rest = remainder[first_h2.start() :].lstrip("\n")
    else:
        intro = remainder.rstrip()
        rest = ""

    chunks = [title.rstrip(), ""]
    if intro:
        chunks.append(intro)
        chunks.append("")
    chunks.append(block.rstrip())
    if rest:
        chunks.append("")
        chunks.append(rest.rstrip())
    return clean_whitespace("\n".join(chunks))


def main() -> None:
    skill_files = sorted(ROOT.glob("*/SKILL.md"))
    updated = 0
    for skill_file in skill_files:
        original = skill_file.read_text(encoding="utf-8")
        frontmatter, body = split_frontmatter(original)
        description = extract_description(frontmatter)
        block = build_block(skill_file.parent.name, description, body)
        updated_text = frontmatter + insert_block(body, block)
        if updated_text != original:
            skill_file.write_text(updated_text, encoding="utf-8", newline="\n")
            updated += 1
    print(f"Updated {updated} skills")


if __name__ == "__main__":
    main()
