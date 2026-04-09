class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)

        for i in range(len(profit)):
            curRow = [0] * (capacity + 1)
            for c in range(1, capacity + 1):
                skip = dp[c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + curRow[c - weight[i]]
                curRow[c] = max(skip, include)

            dp = curRow
        return dp[capacity]
      
      
      
      
      
      
      
      
      
      
        # # Bottom Up DP Solution
        # # TC: O(n * m), SC: O(n * m)
        # N, M = len(profit), capacity
        # dp = [[0] * (M + 1) for _ in range(N)]

        # for i in range(N):
        #     dp[i][0] = 0

        # for c in range(M + 1):
        #     if weight[0] <= c:
        #         dp[0][c] = (c // weight[0]) * profit[0]

        # for i in range(1, N):
        #     for c in range(1, M + 1):
        #         skip = dp[i - 1][c]
        #         include = 0
        #         if c - weight[i] >= 0:
        #             include = profit[i] + dp[i][c - weight[i]]
        #         dp[i][c] = max(include, skip)

        # return dp[N - 1][M]    
    
    
    
    
    
    
    
    
    
    
    
    #     # Memoization
    #     cache = [[-1] * (capacity + 1) for _ in range(len(profit))]

    #     return self.dfs(0, profit, weight, capacity, cache)

    # def dfs(self, i, profit, weight, capacity, cache):
    #     if i == len(profit):
    #         return 0

    #     if cache[i][capacity] != -1:
    #         return cache[i][capacity]

    #     # skip item
    #     cache[i][capacity] = self.dfs(i + 1, profit, weight, capacity, cache)

    #     # include item
    #     newCap = capacity - weight[i]
    #     if newCap >= 0:
    #         p = profit[i] + self.dfs(i, profit, weight, newCap, cache)
    #         cache[i][capacity] = max(cache[i][capacity], p)

    #     return cache[i][capacity]




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
