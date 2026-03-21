def shortest_path(tree, source, destination):
    # Check if both the source and destination nodes are present in the tree
    if source not in tree or destination not in tree:
        return "Source or destination node not found in the tree"

    visited = []

    def dfs(node, dest, path):
        visited.append(node)
        if node == dest:
            return path + [node], len(visited)

        for neighbor in tree[node]:
            if neighbor not in visited:
                new_path, num_nodes = dfs(neighbor, dest, path + [node])
                if new_path is not None:
                    return new_path, num_nodes

        return None, len(visited)

    # Call the helper function with source and destination nodes as arguments
    path, num_nodes = dfs(source, destination, [])

    # If no path was found, return an error message
    if path is None:
        return "No path found between source and destination"

    return path, num_nodes