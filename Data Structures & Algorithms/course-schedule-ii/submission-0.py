class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visit = set()
        cycle = set()
        res = []

        for c in range(numCourses):
            if not self.dfs(c, adj, visit, cycle, res):
                return []
        return res

    def dfs(self, crs, adj, visit, cycle, res):
        if crs in visit:
            return True
        
        if crs in cycle:
            return False

        cycle.add(crs)
        for pre in adj[crs]:
            if not self.dfs(pre, adj, visit, cycle, res):
                return False
        cycle.remove(crs)
        visit.add(crs)
        res.append(crs)

        return True
        
    
    