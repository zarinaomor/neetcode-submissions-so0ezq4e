class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since python has only minHeap, we multiply each stone to -1, so minHeap becomes Max Heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        stones.append(0)
        
        while len(stones) > 1:
            # x is for largest stone in heap
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            # since stones multiplied to -1, we need to do y > x. If potive number would be y < x
            if y > x:
                heapq.heappush(stones, x - y)
        # since the stones currently negative numbers, return positive by abs
        
        return abs(stones[0])
        