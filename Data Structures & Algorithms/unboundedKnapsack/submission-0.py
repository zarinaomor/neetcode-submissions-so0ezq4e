class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(i, capacity):
            if i == len(profit):
                return 0

            # skip item
            maxProfit = dfs(i + 1, capacity)

            # include item
            newCap = capacity - weight[i]
            if newCap >= 0:
                p = profit[i] + dfs(i, newCap)
                maxProfit = max(maxProfit, p)

            return maxProfit
        
        return dfs(0, capacity)
