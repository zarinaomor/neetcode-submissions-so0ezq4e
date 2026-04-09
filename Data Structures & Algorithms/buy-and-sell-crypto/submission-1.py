class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(l + 1, len(prices)):
            if prices[l] < prices[r]:
                curProfit = prices[r] - prices[l]
                res = max(res, curProfit)
            else:
                l = r
        return res



        