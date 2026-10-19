# Boundaries

## Supported

- Reading, locating, comparing and validating OOXML packages (pptx, docx, xlsx).
- Constrained apply: one proven operation per call, always to a new output file.
- Local execution with one activated delivery license; works offline afterwards.

## Not supported

- Unconstrained editing; a free-form "rewrite my document" request is out of scope.
- Uploading documents to a cloud service. This skill is not a cloud processor.
- Unverified platforms (the delivery supports the verified macOS/arm64/Python ABI only).

## Refusals are information

When the engine refuses (for example a broken package or an unauthorized
operation), report the real reason and the next step instead of forcing a result.
Forged, edited, expired or wrong-artifact licenses are refused.

## Trigger examples

- "分析合同.docx" → man(operations) → inspect → locate → view → validate → report.
- "把这个单元格 DRAFT 改成 REVIEWED" → locate the cell → apply to a new file → validate.
- "这个损坏的 pptx 打不开" → inspect refuses → report the real reason; do not guess.
