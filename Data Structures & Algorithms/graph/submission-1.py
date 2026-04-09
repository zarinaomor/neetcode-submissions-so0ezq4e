
class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:

        if src not in self.adjList:
            self.adjList[src] = []
        if dst not in self.adjList:
            self.adjList[dst] = []
        self.adjList[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList:
            return False
        
        # remove the edge
        self.adjList[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        # DFS
        visit = set()
        return self.dfs(src, dst, visit)

    def dfs(self, src, dst, visit):
        
        if src == dst:
            return True

        visit.add(src)
        for neigh in self.adjList[src]:
            if neigh not in visit:
                if self.dfs(neigh, dst, visit):
                    return True
        return False





        # BFS
        # q = deque()
        # visit = set()
        # q.append(src)
        # visit.add(src)

        # while q:
        #     for i in range(len(q)):
        #         cur = q.popleft()
        #         if cur == dst:
        #             return True
        #         for neigh in self.adjList[cur]:
        #             if neigh not in visit:
        #                 visit.add(neigh)
        #                 q.append(neigh)

        # return False










