# CLI reference

Every operation takes one JSON object via `--params '<JSON>'` (or `--params-file <path>`).
There is no `key=value` syntax.

## Setup and diagnostics

- `ooxml --version` — CLI version.
- `ooxml status` — runtime artifact plus activation state (active / license_missing).
- `ooxml activate --license /abs/delivery-license.json` — install a delivery license.

## Operations

- `ooxml man` — operation catalogue (`{"topic": "operations", "output": "summary"}`).
- `ooxml inspect` — document overview; add `"view": "layout"` for PPTX layouts.
- `ooxml locate` — target paths (`{"view": "slides", "limit": 20}`); paginate.
- `ooxml view` — read a target (`mode`: `detail/summary/text/xml`); `target` may be an array.
- `ooxml diff` — compare two documents (`modes`: `["opc","xml","semantic"]`).
- `ooxml validate` — `{"level": "structural"}` or `"semantic"`; always validate first.
- `ooxml apply` — one constrained operation to a NEW output file:
  `{"path": "...", "output_path": "...", "operation_id": "...", "target": "...", "params": {...}}`.

## Fallback rule

Prefer the registered MCP server. Use the CLI when MCP is not reachable, for
diagnostics, and for installation. Both layers share one local runtime and one
license state; there are no separate permissions.
