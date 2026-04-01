class SimpleMarkdownFormatter:
    def __init__(self):
        self.blocks = []

    def add_header(self, text: str, level: int = 1):
        level = max(1, min(level, 6))
        self.blocks.append(f"{'#' * level} {text}")

    def add_paragraph(self, text: str):
        self.blocks.append(text)

    def add_list(self, items: list, ordered: bool = False):
        if ordered:
            for i, item in enumerate(items, 1):
                self.blocks.append(f"{i}. {item}")
        else:
            for item in items:
                self.blocks.append(f"- {item}")

    def add_code_block(self, code: str, language: str = ""):
        self.blocks.append(f"```{language}\n{code}\n```")

    def render(self) -> str:
        return "\n\n".join(self.blocks)