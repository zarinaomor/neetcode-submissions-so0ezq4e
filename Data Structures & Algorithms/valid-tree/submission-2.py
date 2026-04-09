class DSU:
    def __init__(self, n):
        self.comps = n
        self.par = {}
        self.rank = {}

        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        self.comps -= 1

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True
    
    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1
        









        # adj = {i:[] for i in range(n)}
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # visit = set()

        # def dfs(node, parent):
        #     if node in visit:
        #         return False
            
        #     visit.add(node)
        #     for nei in adj[node]:
        #         if nei == parent:
        #             continue
        #         if not dfs(nei, node):
        #             return False
        #     return True

        # return dfs(0, -1) and len(visit) == n
        