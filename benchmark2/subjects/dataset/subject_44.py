class HTMLBuilder:
    def __init__(self):
        self.elements = []

    def p(self, text: str, **kwargs):
        self._add_tag("p", text, kwargs)
        return self

    def a(self, href: str, text: str, **kwargs):
        kwargs["href"] = href
        self._add_tag("a", text, kwargs)
        return self

    def div(self, inner_html: str, **kwargs):
        self._add_tag("div", inner_html, kwargs)
        return self

    def _add_tag(self, tag: str, inner: str, attrs: dict):
        attr_str = " ".join(f'{k}="{v}"' for k, v in attrs.items())
        if attr_str:
            attr_str = " " + attr_str
        self.elements.append(f"<{tag}{attr_str}>{inner}</{tag}>")

    def render(self) -> str:
        return "\n".join(self.elements)