# ooxml-agent-skill

Customer-facing agent skill for the OOXML Client (the MIT-licensed CLI, default
MCP and workflow MCP in `ooxml-stack/ooxml-client`). The skill is agent
guidance: it teaches a customer agent to use the local MCP server first, the
CLI for installation, diagnostics and explicit fallback, and to state the real
boundaries (local execution, constrained apply, correct refusals, offline
after activation).

## Scope of this license

This repository is MIT-licensed. The license covers ONLY the contents of this
repository. It does NOT include and does NOT authorize:

- the proprietary OOXML runtime or the manufactured wheel,
- any license key or delivery license file,
- the private engine repository or its sources,
- any private download service or private delivery credential.

The runtime is delivered separately under its own commercial terms.

## Install

Install the `ooxml/` skill directory into your agent's user-level skill
directory (Claude Code: `~/.claude/skills/ooxml/`; Codex: the user-level skill
directory your agent discovers). Back up a same-named older skill; never
silently overwrite an incompatible version.

## Tests

`python3 -m pytest tests/`
