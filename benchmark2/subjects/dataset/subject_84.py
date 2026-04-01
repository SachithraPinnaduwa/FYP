class WeightedGraph:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_edge(self, u: str, v: str, weight: float):
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.append((weight, u, v))

    def get_mst_kruskal(self) -> list:
        # Kruskal's algorithm
        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}

        def find(item):
            if parent[item] == item:
                return item
            parent[item] = find(parent[item])
            return parent[item]

        def union(set1, set2):
            root1 = find(set1)
            root2 = find(set2)
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

        mst = []
        # Sort edges by weight
        self.edges.sort(key=lambda item: item[0])

        for weight, u, v in self.edges:
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                mst.append((u, v, weight))
                union(root_u, root_v)

        return mst