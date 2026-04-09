class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfs(0, profit, weight, capacity)

    def dfs(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0

        # decision not include
        maxProfit = self.dfs(i + 1, profit, weight, capacity)

        # decision to include 
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfs(i + 1, profit, weight, newCap)
            maxProfit = max(maxProfit, p)

        return maxProfit

