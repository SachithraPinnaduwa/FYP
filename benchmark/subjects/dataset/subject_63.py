class JsonPathExtractor:
    def __init__(self, data: dict):
        self.data = data

    def extract(self, path: str):
        if not path.startswith("$."):
            return None
            
        parts = path[2:].split(".")
        current = self.data
        
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            elif isinstance(current, list) and part.isdigit():
                idx = int(part)
                if 0 <= idx < len(current):
                    current = current[idx]
                else:
                    return None
            else:
                return None
                
        return current