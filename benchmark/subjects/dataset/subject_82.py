class SimpleLDAP:
    def __init__(self):
        self.directory = {"dc=com": {"name": "com", "children": []}}

    def add_entry(self, dn: str, attributes: dict):
        parts = dn.split(",")
        current = self.directory
        
        for i, part in enumerate(reversed(parts)):
            if part not in current:
                if i == len(parts) - 1:
                    current[part] = attributes
                    current[part]["children"] = {}
                else:
                    current[part] = {"children": {}}
            if i < len(parts) - 1:
                if "children" not in current[part]:
                    current[part]["children"] = {}
                current = current[part]["children"]

    def search(self, base_dn: str, filter_key: str, filter_val: str) -> list:
        parts = base_dn.split(",")
        current = self.directory
        
        for part in reversed(parts):
            if part not in current:
                return []
            if "children" in current[part]:
                current = current[part]["children"]
            else:
                current = {part: current[part]}
                break
                
        results = []
        self._dfs_search(current, filter_key, filter_val, results)
        return results

    def _dfs_search(self, node: dict, fk: str, fv: str, results: list):
        for key, attrs in node.items():
            if attrs.get(fk) == fv:
                results.append(attrs)
            if "children" in attrs:
                self._dfs_search(attrs["children"], fk, fv, results)