# MCP reference

The client registers the engine's MCP server over stdio (local only; there is no
remote MCP). Both profiles run on the customer Mac and share one license state.

## Profiles

- default (core): the analysis/constrained-apply tool set registered as `ooxml`.
- workflow: the session workflow tool set registered as `ooxml-workflow`.

## Agent registration

- Claude Code: `ooxml register claude --scope local` (or `--scope project`).
- Codex: `ooxml register codex`.
- Re-run with `--force` to replace an existing registration; back up the previous
  configuration first (the launcher does this).

## Discovery

1. initialize, then `tools/list`.
2. Call the exact returned tool names with the exact returned schemas.
3. The tool collection must match `mcp-contract.json` shipped by the client
   release; a mismatch means the release is inconsistent — stop and report.

## Guarantees

- Execution is local: tools process documents on this Mac.
- Without an activated license the tools refuse; activate first.
- After activation the tools work offline.
