class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # Memoization
        cache = [[-1] * (capacity + 1) for _ in range(len(profit))]

        return self.dfs(0, profit, weight, capacity, cache)

    def dfs(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0

        if cache[i][capacity] != -1:
            return cache[i][capacity]

        # skip item
        cache[i][capacity] = self.dfs(i + 1, profit, weight, capacity, cache)

        # include item
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfs(i, profit, weight, newCap, cache)
            cache[i][capacity] = max(cache[i][capacity], p)

        return cache[i][capacity]




# Brute Force Solution 
# Time Complexity 2^n
        # def dfs(i, capacity):
        #     if i == len(profit):
        #         return 0

        #     # skip item
        #     maxProfit = dfs(i + 1, capacity)

        #     # include item
        #     newCap = capacity - weight[i]
        #     if newCap >= 0:
        #         p = profit[i] + dfs(i, newCap)
        #         maxProfit = max(maxProfit, p)

        #     return maxProfit
        
        # return dfs(0, capacity)
