class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
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
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(len(edges))

        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        return []
        

       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # n = len(edges)
        # adj = {i:[] for i in range(n + 1)}

        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        # visit = set()

        # def dfs(node, parent):
        #     if node in visit:
        #         return True
        #     visit.add(node)
        #     for nei in adj[node]:
        #         if nei == parent:
        #             continue
        #         if dfs(nei, node):
        #             return True
       
        #     return False

        # return [u, v] if dfs(u, -1) else []

       
       
       
       
       
       
       
       
        # parent = [i for i in range(len(edges) + 1)]
        # rank = [1] * (len(edges) + 1)

        # def find(n):
        #     if n != parent[n]:
        #         parent[n] = parent[parent[n]]
        #     return parent[n]

        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)
        #     if p1 == p2:
        #         return False
            
        #     if rank[p1] > rank[p2]:
        #         parent[p2] = p1
        #         rank[p1] += rank[p2]
        #     else:
        #         parent[p1] = p2
        #         rank[p2] += rank[p1]

        #     return True

        # for n1, n2 in edges:
        #     if not union(n1, n2):
        #         return [n1, n2]






