---
name: ooxml
description: Work with Office documents (pptx, docx, xlsx) through the local OOXML MCP
  server and CLI. Use when the user asks to analyze, inspect, locate, compare, validate
  or apply a constrained operation to an Office document, including Chinese requests
  such as 分析/检查/比对/校验/读取/定位/修改 Office 文档.
---

# OOXML document operations (customer skill)

## Priority

1. Default to the local MCP server registered as `ooxml` (tools/list first).
2. Use the `ooxml` CLI for installation, diagnostics and explicit fallback.
3. Documents are processed locally. They are never uploaded to a cloud service.

## Setup check

- `ooxml --version` — the CLI answers with its version.
- `ooxml status` — answers with the runtime artifact and the activation state.
- If either fails, follow README.md (Install with your agent) from the product page.

## Workflow (in order)

1. Catalogue: MCP `ooxml_man` or CLI `ooxml man --params '{"topic": "operations", "output": "summary"}'`
   — list operation IDs and target types; do not read full schemas first.
2. Structure: `ooxml_inspect` or `ooxml inspect --params '{"path": "/abs/x.pptx"}'`.
3. Locate: `ooxml_locate` — reuse the returned target paths; paginate with `limit`/`offset`.
4. Read: `ooxml_view` — `target` may be an array; `mode` is `detail/summary/text/xml`.
5. Apply (changes only): `ooxml_apply` — always write to a NEW output file.
6. Validate: `ooxml_validate` with level `structural` or `semantic`; always validate
   before delivering, and report findings before a result.

## Habits (fail closed)

- Input is read-only: never modify the source file; prove it with an unchanged hash.
- Apply is constrained: one operation, one output file. Reject unconstrained change requests.
- Report the real reason when the engine refuses; never invent an editing capability.
