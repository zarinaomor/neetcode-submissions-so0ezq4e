class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {}
        def dfs(i, total):
            if i >= n:
                return 1 if total == target else 0

            if (i, total) in cache:
                return cache[(i, total)]

            cache[(i, total)] = dfs(i + 1, total - nums[i]) + dfs(i + 1, total + nums[i])
            return cache[(i, total)]
        return dfs(0, 0)








        # def dfs(i, total):
        #     if i >= len(nums):
        #         return total == target

        #     return dfs(i + 1, total - nums[i]) + dfs(i + 1, total + nums[i])

        # return dfs(0, 0)