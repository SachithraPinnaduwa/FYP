class XMLBuilder:
    def __init__(self, root_name: str):
        self.root = root_name
        self.children = []
        self.attributes = {}
        self.text = ""

    def add_attribute(self, key: str, value: str):
        self.attributes[key] = value
        return self

    def add_child(self, name: str):
        child = XMLBuilder(name)
        self.children.append(child)
        return child

    def set_text(self, text: str):
        self.text = text
        return self

    def render(self, indent: int = 0) -> str:
        spaces = "  " * indent
        attrs = " ".join(f'{k}="{v}"' for k, v in self.attributes.items())
        attr_str = f" {attrs}" if attrs else ""
        
        if not self.children and not self.text:
            return f"{spaces}<{self.root}{attr_str} />"
            
        result = [f"{spaces}<{self.root}{attr_str}>"]
        if self.text:
            result.append(f"{spaces}  {self.text}")
        for child in self.children:
            result.append(child.render(indent + 1))
            
        result.append(f"{spaces}</{self.root}>")
        return "\n".join(result)