class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False

            if adj[crs] == []:
                return True

            visit.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            adj[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



        
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #     adj = {}
    #     for i in range(numCourses):
    #         adj[i] = []

    #     for crs, pre in prerequisites:
    #         adj[crs].append(pre)

    #     visit = set()

    #     for c in range(numCourses):
    #         if not self.dfs(c, adj, visit):
    #             return False
    #     return True


    # def dfs(self, crs, adj, visit):
    #     if crs in visit:
    #         return False

    #     if adj[crs] == []:
    #         return True

    #     visit.add(crs)
    #     for pre in adj[crs]:
    #         if not self.dfs(pre, adj, visit):
    #             return False
    #     visit.remove(crs)
    #     adj[crs] = []
    #     return True
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # preMap = {i: [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)

        # visit = set()
        # def dfs(crs):
        #     # if loop is detected return false
        #     if crs in visit:
        #         return False
        #     if preMap[crs] == []:
        #         return True
            
        #     visit.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visit.remove(crs)
        #     preMap[crs] = []
        #     return True

        # # for loop needs here incase theres is disconnected node
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True
