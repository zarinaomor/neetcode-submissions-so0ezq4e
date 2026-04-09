class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []

        for src, dst, w in edges:
            adj[src].append([dst, w])
            adj[dst].append([src, w])

        minHeap = []
        for neighbor, weight in adj[1]:
            heapq.heappush(minHeap, [weight, 1, neighbor])

        mst = 0
        visit = set()
        visit.add(1)

        while minHeap:
            w, src, dst = heapq.heappop(minHeap)
            if dst in visit:
                continue
            mst += w
            visit.add(dst)

            for neighbor, weight in adj[dst]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, dst, neighbor])

        if len(visit) < n:
            return -1

        return mst




