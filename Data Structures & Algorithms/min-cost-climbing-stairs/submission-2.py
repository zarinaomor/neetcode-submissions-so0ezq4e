class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom-Up approach. Time: O(n), Space: O(1)
        n = len(cost)
        for i in range(n - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        
        return min(cost[0], cost[1])


        # Bottom-Up approach Time: O(n), Space: O(n)
        # n = len(cost)
        # dp = [0] * (n + 1)
        
        # for i in range(2, n + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        # return dp[n]



        # Memoization Time: O(n) Space: O(n)
        # n = len(cost)
        # cache = {}

        # def dfs(i):
        #     if i >= len(cost):
        #         return 0

        #     if i in cache:
        #         return cache[n]

        #     cache[n] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return cache[n]
        # return min(dfs(0), dfs(1))

        # Recursion/dfs O(2n) space O(n)
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
                
        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))

        # return min(dfs(0), dfs(1))


            
        
        
        