class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = float('inf')

            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))

            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins == float('inf') else minCoins
















# # Brute Force solution
#         def dfs(amount):
#             if amount == 0:
#                 return 0

#             res = float('inf')
#             for coin in coins:
#                 if amount - coin >=0:
#                     res = min(res, 1 + dfs(amount - coin))

#             return res

#         minCoins = dfs(amount)

#         return -1 if minCoins >= float('inf') else minCoins