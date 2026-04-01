class URLBuilder:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.paths = []
        self.query_params = {}

    def add_path(self, path: str):
        self.paths.append(path.strip('/'))
        return self

    def add_query(self, key: str, value: str):
        self.query_params[key] = str(value)
        return self

    def build(self) -> str:
        url = self.base_url
        if self.paths:
            url += '/' + '/'.join(self.paths)
            
        if self.query_params:
            import urllib.parse
            qs = urllib.parse.urlencode(self.query_params)
            url += '?' + qs
            
        return url