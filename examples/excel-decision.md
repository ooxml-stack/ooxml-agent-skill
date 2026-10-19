# Excel: record a decision cell (proven)

Task: record DRAFT → REVIEWED in one intake cell.

1. `ooxml_locate` the cell (`sheets[0].cells[A1]` in the proven task).
2. `ooxml_apply` — `cell.set_value` with the string value and `value_type: "string"`,
   output to a NEW workbook.
3. `ooxml_validate` the output.

Report the unchanged input and the new output; the original stays untouched.
