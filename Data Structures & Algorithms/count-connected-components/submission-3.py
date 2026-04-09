class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
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
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res


















        # adj = {i:[] for i in range(n)}

        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # visit = set()
        # res = 0

        # def dfs(node):
        #     if node in visit:
        #         return
        #     visit.add(node)
        #     for nei in adj[node]:
        #         dfs(nei)
        
        # for node in range(n):
        #     if node not in visit:
        #         dfs(node)
        #         res += 1
        # return res
        