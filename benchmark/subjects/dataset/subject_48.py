class SimpleMarkdownTable:
    def __init__(self, headers: list):
        self.headers = [str(h) for h in headers]
        self.rows = []

    def add_row(self, row: list):
        self.rows.append([str(c) for c in row])

    def render(self) -> str:
        all_rows = [self.headers] + self.rows
        col_widths = [max(len(r[i]) if i < len(r) else 0 for r in all_rows) for i in range(len(self.headers))]

        result = []
        # Header
        result.append("| " + " | ".join(h.ljust(w) for h, w in zip(self.headers, col_widths)) + " |")
        # Separator
        result.append("|" + "|".join("-" * (w + 2) for w in col_widths) + "|")
        # Rows
        for row in self.rows:
            padded_row = [row[i].ljust(col_widths[i]) if i < len(row) else " " * col_widths[i] 
                          for i in range(len(self.headers))]
            result.append("| " + " | ".join(padded_row) + " |")

        return "\n".join(result)