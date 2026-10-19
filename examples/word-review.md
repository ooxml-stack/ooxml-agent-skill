# Word: review a draft (proven)

Task: flip one draft line to REVIEWED and deliver a validated new file.

1. `ooxml_inspect` on the docx (structure overview).
2. `ooxml_locate` the target paragraph (reuse the returned path).
3. `ooxml_apply` — `text.set_container` on the located paragraph, output to a
   NEW file.
4. `ooxml_validate` the output (structural).
5. Report: unchanged input hash, new output path, validation result.

The engine refuses an unconstrained rewrite; apply is one operation per call.
