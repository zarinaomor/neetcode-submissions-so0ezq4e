class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0

        for r in range(l + 1, len(prices)):
            if prices[l] < prices[r]:
                curP = prices[r] - prices[l]
                maxP = max(maxP, curP)
            else:
                l = r
        return maxP

        