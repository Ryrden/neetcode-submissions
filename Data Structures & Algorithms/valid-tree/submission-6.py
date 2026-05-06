class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        graph = defaultdict(list)
        for v,w in edges:
            graph[v].append(w)
            graph[w].append(v)
        
        visited = set()

        def has_cycle(node, prev):
            if node in visited:
                return True
            
            visited.add(node)
            for adj in graph[node]:
                if adj == prev:
                    continue
                if has_cycle(adj, node):
                    return True
            return False
        return not has_cycle(0, -1) and n == len(visited)