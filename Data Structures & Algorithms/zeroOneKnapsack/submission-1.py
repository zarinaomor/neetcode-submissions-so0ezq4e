class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        return self.helper(0, profit, weight, capacity, cache)

    def helper(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0

        if cache[i][capacity] != -1:
            return cache[i][capacity]

        # skip item
        cache[i][capacity] = self.helper(i + 1, profit, weight, capacity, cache)

        # include item
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + (self.helper(i + 1, profit, weight, newCap, cache))
            # Compute the max
            cache[i][capacity] = max(cache[i][capacity], p)

        return cache[i][capacity]

   
   
   
   
   
   
   
   
   
   
    #     return self.dfs(0, profit, weight, capacity)

    # def dfs(self, i, profit, weight, capacity):
    #     if i == len(profit):
    #         return 0

    #     # decision not include
    #     maxProfit = self.dfs(i + 1, profit, weight, capacity)

    #     # decision to include 
    #     newCap = capacity - weight[i]
    #     if newCap >= 0:
    #         p = profit[i] + self.dfs(i + 1, profit, weight, newCap)
    #         maxProfit = max(maxProfit, p)

    #     return maxProfit

