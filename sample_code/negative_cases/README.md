# Negative Test Cases

Each file in this directory is designed to trigger a specific validation
error from the `validate_code_input()` check in `backend/app.py`.

| File | Validation path triggered | Expected error snippet |
|------|--------------------------|------------------------|
| `empty.py` | Check 1 – empty input | *"Input code is empty…"* |
| `whitespace_only.py` | Check 1 – blank input | *"Input code is empty…"* |
| `no-code.py` | Check 2 – syntax error with prose on failing line | *"The input appears to contain non-Python text…"* |
| `syntax_error.py` | Check 2 – genuine syntax error | *"Syntax error on line X: …"* |
| `prose_in_middle.py` | Check 3 – prose-like lines inside otherwise valid code | *"The input contains non-Python text. Detected prose-like content at: …"* |
| `prose_at_top.py` | Check 2 or 3 – prose before code | *"The input appears to contain non-Python text…"* |
| `prose_at_bottom.py` | Check 3 – prose appended after code | *"The input contains non-Python text. Detected prose-like content at: …"* |
| `only_comments.py` | Check 4 – no testable constructs | *"No testable Python constructs…"* |
| `only_strings.py` | Check 4 – only bare string literals | *"The input contains only plain text strings…"* |
