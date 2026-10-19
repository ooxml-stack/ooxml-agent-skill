"""Customer skill package contracts: manifest, frontmatter, no secrets."""

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

FRONTMATTER = re.compile(r"^---\n(.+?)\n---\n", re.DOTALL)


def test_manifest_schema():
    manifest = json.loads((REPO / "skill-manifest.json").read_text())
    assert manifest["name"] == "ooxml"
    assert re.match(r"^\d+\.\d+\.\d+$", manifest["version"])
    assert manifest["requires_client"] == ">=0.1.50,<0.2.0"
    assert manifest["requires_mcp_contract"] == "1"


def test_skill_frontmatter_and_priority():
    skill = (REPO / "SKILL.md").read_text()
    match = FRONTMATTER.match(skill)
    assert match is not None
    assert "name: ooxml" in match.group(1)
    assert "local MCP" in skill and "never uploaded" in skill


def test_no_secrets_or_internal_paths():
    banned = re.compile(r"fly\.dev|vercel\.app|/Users/|\.delivery-evidence|\.worktrees|token|PEM")
    for path in REPO.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert not banned.search(text), f"banned content in {path.name}"


def test_examples_cover_the_proven_set():
    examples = sorted(p.name for p in (REPO / "examples").glob("*.md"))
    assert examples == ["excel-decision.md", "pptx-boundary-refusal.md", "word-review.md"]
    assert "proven" in (REPO / "examples/pptx-boundary-refusal.md").read_text()


def test_references_present():
    for name in ("cli.md", "mcp.md", "boundaries.md"):
        assert (REPO / "references" / name).exists()
