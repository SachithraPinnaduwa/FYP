class DependencyGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, name: str):
        if name not in self.graph:
            self.graph[name] = []

    def add_dependency(self, name: str, dep: str):
        self.add_node(name)
        self.add_node(dep)
        self.graph[name].append(dep)

    def resolve(self, node: str) -> list:
        resolved = []
        visited = set()
        path = set()

        def dfs(current: str):
            if current in path:
                raise ValueError(f"Circular dependency detected at {current}")
            if current not in visited:
                visited.add(current)
                path.add(current)
                for edge in self.graph.get(current, []):
                    dfs(edge)
                path.remove(current)
                resolved.append(current)

        dfs(node)
        return resolved