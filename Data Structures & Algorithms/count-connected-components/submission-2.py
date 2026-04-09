class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1, p2, = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1 
            self.rank[p1] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        res = n
        for u, v in edges:
            if unionFind.union(u, v):
                res -= 1
        return res




















        # self.parent = {}
        # self.rank = {}

        # for i in range(n):
        #     self.parent[i] = i
        #     self.rank[i] = 1

        # def find(n):
        #     if n != self.parent[n]:
        #         self.parent[n] = find(self.parent[n])
        #     return self.parent[n]

        # def union(x, y):
        #     p1, p2 = find(x), find(y)
        #     if p1 == p2:
        #         return False

        #     if self.rank[p1] > self.rank[p2]:
        #         self.parent[p2] = p1
        #         self.rank[p1] += self.rank[p2]
        #     else:
        #         self.parent[p1] = p2
        #         self.rank[p2] += self.rank[p1]

        #     return True

        # components = n
        # for x, y in edges:
        #     if union(x, y):
        #         components -= 1
        # return components


        