class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []

        for src, dst in edges:
            adj[src].append(dst)

        topSort = []
        visit = set()
        visiting = set() #detect cycle
        for i in range(n):
            if not self.dfs(i, adj, topSort, visit, visiting):
                return []
        topSort.reverse()

        return topSort

    def dfs(self, src, adj, topSort, visit, visiting):
        if src in visit:
            return True

        if src in visiting:
            return False

        visiting.add(src)
        for nei in adj[src]:
            if not self.dfs(nei, adj, topSort, visit, visiting):
                return False

        visiting.remove(src)
        visit.add(src)
        topSort.append(src)

        return True

