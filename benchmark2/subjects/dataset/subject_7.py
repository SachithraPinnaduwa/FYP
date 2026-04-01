import heapq
class Graph:
    def __init__(self): self.edges = {}
    def add_edge(self, u, v, w):
        self.edges.setdefault(u, {})[v] = w
        self.edges.setdefault(v, {})
    def shortest_path(self, start, end):
        distances = {n: float("inf") for n in self.edges}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            d, node = heapq.heappop(pq)
            if node == end: break
            for neighbor, weight in self.edges[node].items():
                if d + weight < distances[neighbor]:
                    distances[neighbor] = d + weight
                    heapq.heappush(pq, (distances[neighbor], neighbor))
        return distances[end]
