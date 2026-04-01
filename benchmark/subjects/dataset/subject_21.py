class SimpleTemplate:
    def __init__(self, template_str: str):
        self.template_str = template_str

    def render(self, context: dict) -> str:
        result = self.template_str
        for key, value in context.items():
            result = result.replace(f"{{{{{key}}}}}", str(value))
        return result