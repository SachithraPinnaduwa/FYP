import re
class Router:
    def __init__(self): self.routes = []
    def add(self, method, pattern, handler):
        self.routes.append((re.compile(pattern), method.upper(), handler))
    def handle(self, method, path):
        for p, m, handler in self.routes:
            if m == method.upper() and p.match(path):
                return handler(p.match(path).groupdict())
        return "404 Not Found"
