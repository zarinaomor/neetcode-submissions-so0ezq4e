class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [[0] * (M + 1) for _ in range(N)]

        # Fill the first row to avoid edge cases
        for r in range(N):
            dp[r][0] = 0

        # Fill the first column to avoid edge cases
        for c in range(M + 1):
            if c >=weight[0]:
                dp[0][c] = profit[0]

        for r in range(1, N):
            for c in range(1, M + 1):
                skip = dp[r - 1][c]
                include = 0
                if c - weight[r] >= 0:
                    include = profit[r] + dp[r - 1][c - weight[r]]
                dp[r][c] = max(include, skip)

        return dp[N - 1][M]

        

    
    
    
    
    
    
    
    
    
    
    
    
    #     N, M = len(profit), capacity
    #     cache = [[-1] * (M + 1) for _ in range(N)]
    #     return self.helper(0, profit, weight, capacity, cache)

    # def helper(self, i, profit, weight, capacity, cache):
    #     if i == len(profit):
    #         return 0

    #     if cache[i][capacity] != -1:
    #         return cache[i][capacity]

    #     # skip item
    #     cache[i][capacity] = self.helper(i + 1, profit, weight, capacity, cache)

    #     # include item
    #     newCap = capacity - weight[i]
    #     if newCap >= 0:
    #         p = profit[i] + (self.helper(i + 1, profit, weight, newCap, cache))
    #         # Compute the max
    #         cache[i][capacity] = max(cache[i][capacity], p)

    #     return cache[i][capacity]

   
   
   
   
   
   
   
   
   
   
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

