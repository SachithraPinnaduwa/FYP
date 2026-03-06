"""
Graph module - Subject for test generation benchmarking.
Contains graph data structure and common graph algorithms.
"""

from typing import Any, Dict, List, Optional, Set, Tuple
from collections import deque


class GraphError(Exception):
    """Base exception for graph errors."""
    pass


class NodeNotFoundError(GraphError):
    """Raised when a node is not found in the graph."""
    pass


class Graph:
    """
    An adjacency-list based graph implementation supporting both
    directed and undirected, weighted and unweighted graphs.
    """

    def __init__(self, directed: bool = False):
        """
        Initialize an empty graph.

        Args:
            directed: If True, the graph is directed
        """
        self._adj: Dict[Any, Dict[Any, float]] = {}
        self._directed = directed

    @property
    def is_directed(self) -> bool:
        return self._directed

    @property
    def nodes(self) -> List[Any]:
        """Return a list of all nodes."""
        return list(self._adj.keys())

    @property
    def num_nodes(self) -> int:
        return len(self._adj)

    @property
    def num_edges(self) -> int:
        total = sum(len(neighbors) for neighbors in self._adj.values())
        if not self._directed:
            total //= 2
        return total

    def add_node(self, node: Any) -> None:
        """Add a node to the graph."""
        if node not in self._adj:
            self._adj[node] = {}

    def remove_node(self, node: Any) -> None:
        """
        Remove a node and all its edges.

        Raises:
            NodeNotFoundError: If the node does not exist
        """
        if node not in self._adj:
            raise NodeNotFoundError(f"Node '{node}' not found")
        # Remove all edges to this node
        for neighbor in list(self._adj[node]):
            if neighbor in self._adj and node in self._adj[neighbor]:
                del self._adj[neighbor][node]
        del self._adj[node]

    def add_edge(self, u: Any, v: Any, weight: float = 1.0) -> None:
        """
        Add an edge between u and v.

        Args:
            u: Source node
            v: Destination node
            weight: Edge weight (default 1.0)
        """
        self.add_node(u)
        self.add_node(v)
        self._adj[u][v] = weight
        if not self._directed:
            self._adj[v][u] = weight

    def remove_edge(self, u: Any, v: Any) -> None:
        """
        Remove the edge between u and v.

        Raises:
            NodeNotFoundError: If either node doesn't exist
            GraphError: If the edge doesn't exist
        """
        if u not in self._adj:
            raise NodeNotFoundError(f"Node '{u}' not found")
        if v not in self._adj:
            raise NodeNotFoundError(f"Node '{v}' not found")
        if v not in self._adj[u]:
            raise GraphError(f"Edge ({u}, {v}) does not exist")
        del self._adj[u][v]
        if not self._directed:
            del self._adj[v][u]

    def has_node(self, node: Any) -> bool:
        """Check if a node exists."""
        return node in self._adj

    def has_edge(self, u: Any, v: Any) -> bool:
        """Check if an edge exists."""
        return u in self._adj and v in self._adj[u]

    def neighbors(self, node: Any) -> List[Any]:
        """
        Get neighbors of a node.

        Raises:
            NodeNotFoundError: If the node doesn't exist
        """
        if node not in self._adj:
            raise NodeNotFoundError(f"Node '{node}' not found")
        return list(self._adj[node].keys())

    def degree(self, node: Any) -> int:
        """
        Get the degree of a node.

        Raises:
            NodeNotFoundError: If the node doesn't exist
        """
        if node not in self._adj:
            raise NodeNotFoundError(f"Node '{node}' not found")
        return len(self._adj[node])

    def get_weight(self, u: Any, v: Any) -> float:
        """
        Get the weight of an edge.

        Raises:
            GraphError: If the edge doesn't exist
        """
        if not self.has_edge(u, v):
            raise GraphError(f"Edge ({u}, {v}) does not exist")
        return self._adj[u][v]

    def bfs(self, start: Any) -> List[Any]:
        """
        Breadth-first search traversal.

        Args:
            start: Starting node

        Returns:
            List of nodes in BFS order

        Raises:
            NodeNotFoundError: If start node doesn't exist
        """
        if start not in self._adj:
            raise NodeNotFoundError(f"Node '{start}' not found")
        visited = set()
        result = []
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in sorted(self._adj[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start: Any) -> List[Any]:
        """
        Depth-first search traversal.

        Args:
            start: Starting node

        Returns:
            List of nodes in DFS order

        Raises:
            NodeNotFoundError: If start node doesn't exist
        """
        if start not in self._adj:
            raise NodeNotFoundError(f"Node '{start}' not found")
        visited = set()
        result = []

        def _dfs(node):
            visited.add(node)
            result.append(node)
            for neighbor in sorted(self._adj[node]):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return result

    def shortest_path(self, start: Any, end: Any) -> Optional[List[Any]]:
        """
        Find the shortest path between two nodes using BFS (unweighted).

        Returns:
            List of nodes forming the shortest path, or None if no path exists

        Raises:
            NodeNotFoundError: If either node doesn't exist
        """
        if start not in self._adj:
            raise NodeNotFoundError(f"Node '{start}' not found")
        if end not in self._adj:
            raise NodeNotFoundError(f"Node '{end}' not found")

        if start == end:
            return [start]

        visited = {start}
        queue = deque([(start, [start])])
        while queue:
            node, path = queue.popleft()
            for neighbor in self._adj[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    if neighbor == end:
                        return new_path
                    visited.add(neighbor)
                    queue.append((neighbor, new_path))
        return None

    def is_connected(self) -> bool:
        """
        Check if the graph is connected (all nodes reachable from any node).
        For directed graphs, checks weak connectivity.
        """
        if self.num_nodes == 0:
            return True
        start = next(iter(self._adj))
        visited = set(self.bfs(start))
        return len(visited) == self.num_nodes

    def has_cycle(self) -> bool:
        """Check if the graph contains a cycle."""
        visited: Set[Any] = set()
        rec_stack: Set[Any] = set()

        def _has_cycle(node: Any, parent: Any = None) -> bool:
            visited.add(node)
            rec_stack.add(node)
            for neighbor in self._adj[node]:
                if neighbor not in visited:
                    if _has_cycle(neighbor, node):
                        return True
                elif self._directed and neighbor in rec_stack:
                    return True
                elif not self._directed and neighbor != parent:
                    return True
            rec_stack.discard(node)
            return False

        for node in self._adj:
            if node not in visited:
                if _has_cycle(node):
                    return True
        return False

    def edges(self) -> List[Tuple[Any, Any, float]]:
        """Return all edges as (u, v, weight) tuples."""
        result = []
        seen = set()
        for u in self._adj:
            for v, w in self._adj[u].items():
                if self._directed or (v, u) not in seen:
                    result.append((u, v, w))
                    seen.add((u, v))
        return result

    def __repr__(self) -> str:
        kind = "Directed" if self._directed else "Undirected"
        return f"Graph({kind}, {self.num_nodes} nodes, {self.num_edges} edges)"
