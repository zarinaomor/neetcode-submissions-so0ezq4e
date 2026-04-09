class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Memoization Time: O(n) Space: O(n)
        n = len(cost)
        cache = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i in cache:
                return cache[n]

            cache[n] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return cache[n]
        return min(dfs(0), dfs(1))

        # Recursion/dfs O(2n) space O(n)
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
                
        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))

        # return min(dfs(0), dfs(1))


            
        
        
        