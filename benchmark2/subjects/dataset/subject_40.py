class TopologicalSorter:
    def __init__(self):
        self.graph = {}
        self.in_degree = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
            self.in_degree.setdefault(u, 0)
        if v not in self.graph:
            self.graph[v] = []
            self.in_degree.setdefault(v, 0)
            
        self.graph[u].append(v)
        self.in_degree[v] += 1

    def sort(self) -> list:
        queue = [node for node, degree in self.in_degree.items() if degree == 0]
        result = []
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            
            for neighbor in self.graph.get(node, []):
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(result) != len(self.in_degree):
            raise ValueError("Graph contains a cycle")
        return result