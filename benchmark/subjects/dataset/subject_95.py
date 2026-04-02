from collections import defaultdict

def minimum_cost_arborescence(num_vertices, num_edges, root, edges):
    in_edges = defaultdict(set)
    out_edges = defaultdict(set)
    
    for (s, t, w) in edges:
        in_edges[t].add((w, s))
        out_edges[s].add((w, t))
    
    def chu_liu_edmond(vertices, cycle_cost):
        nonlocal in_edges, out_edges, num_vertices, root
        total_cost = cycle_cost
        prev_v = {v: None for v in vertices}
        next_vs = {v: set() for v in vertices}
        
        for t in vertices:
            if t == root:
                continue
            (min_in_w, min_in_s) = min(in_edges[t])
            total_cost += min_in_w
            prev_v[t] = min_in_s
            next_vs[min_in_s].add(t)
        
        visited = {root}
        queue = set(next_vs[root])
        
        while queue:
            t = queue.pop()
            visited.add(t)
            queue.update(next_vs[t])
        
        cycles = []
        for i in vertices:
            if i in visited:
                continue
            cycle_vertices = set()
            while i not in visited:
                visited.add(i)
                cycle_vertices.add(i)
                i = prev_v[i]
            if i not in cycle_vertices:
                continue
            (cycle_vertices, j) = ({i}, prev_v[i])
            while j != i:
                cycle_vertices.add(j)
                j = prev_v[j]
            cycles.append(cycle_vertices)
        
        if not cycles:
            return total_cost
        
        for cycle in cycles:
            vertices.difference_update(cycle)
            vertices.add(num_vertices)
            for v in cycle:
                prev_e_cost = min(in_edges[v])[0]
                cycle_cost += prev_e_cost
                for (w, t) in out_edges[v]:
                    if t in vertices:
                        out_edges[num_vertices].add((w, t))
                        in_edges[t].remove((w, v))
                        in_edges[t].add((w, num_vertices))
                for (w, s) in in_edges[v]:
                    if s in vertices:
                        new_w = w - prev_e_cost
                        in_edges[num_vertices].add((new_w, s))
                        out_edges[s].remove((w, v))
                        out_edges[s].add((new_w, num_vertices))
                del in_edges[v]
                del out_edges[v]
            num_vertices += 1
        
        return chu_liu_edmond(vertices, cycle_cost)
    
    return chu_liu_edmond(set(range(num_vertices)), 0)