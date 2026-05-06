class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            if n1 == parent[n1]:
                return n1
            return find(parent[n1])
        
        def union(n1,n2):
            n1, n2 = find(n1), find(n2)
            if n1 == n2:
                return 0
            parent[n1] = n2
            return 1

        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)
        return res