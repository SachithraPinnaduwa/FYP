class ConfigValidator:
    def __init__(self, schema): self.schema = schema
    def validate(self, config):
        if not isinstance(config, dict): return False
        for k, v in self.schema.get("required", []):
            if k not in config: return False
        return True
