class JsonPatch:
    def __init__(self, document: dict):
        import copy
        self.doc = copy.deepcopy(document)

    def apply(self, patch: list) -> dict:
        for op in patch:
            if op["op"] == "add":
                self._add(op["path"], op["value"])
            elif op["op"] == "replace":
                self._replace(op["path"], op["value"])
            elif op["op"] == "remove":
                self._remove(op["path"])
        return self.doc

    def _resolve_path(self, path: str):
        parts = path.strip("/").split("/")
        if not parts or parts[0] == "":
            return self.doc, None
        
        current = self.doc
        for part in parts[:-1]:
            if part in current:
                current = current[part]
            else:
                raise ValueError(f"Path not found: {path}")
        return current, parts[-1]

    def _add(self, path: str, value: any):
        parent, key = self._resolve_path(path)
        if key is None:
            self.doc = value
        else:
            parent[key] = value

    def _replace(self, path: str, value: any):
        parent, key = self._resolve_path(path)
        if key not in parent:
            raise KeyError(f"Key not found for replace: {path}")
        parent[key] = value

    def _remove(self, path: str):
        parent, key = self._resolve_path(path)
        if key in parent:
            del parent[key]