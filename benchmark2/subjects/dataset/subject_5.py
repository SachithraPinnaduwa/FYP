import re
class MarkdownParser:
    def __init__(self):
        self.rules = [
            (re.compile(r"\*\*(.*?)\*\*"), r"<strong>\1</strong>"),
            (re.compile(r"\*(.*?)\*"), r"<em>\1</em>"),
            (re.compile(r"#(.*?)$", re.MULTILINE), r"<h1>\1</h1>")
        ]
    def parse(self, text: str) -> str:
        for p, r in self.rules:
            text = p.sub(r, text)
        return text
