class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for r in range(1, n + 1):
            for c in range(1, target + 1):
                skip = dp[r - 1][c]
                include = False
                if c - nums[r - 1] >= 0:
                    include = dp[r - 1][c - nums[r - 1]]
                dp[r][c] = include or skip

        return dp[n][target]
















        # if sum(nums) % 2 != 0:
        #     return False

        # target = sum(nums) // 2

        # cache = [[-1] * (target + 1) for _ in range(len(nums) + 1)]


        # def dfs(i, target):
        #     if target == 0:
        #         return True

        #     if target < 0 or i >= len(nums):
        #         return False

        #     if cache[i][target] != -1:
        #         return cache[i][target]

        #     cache[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])

        #     return cache[i][target]

        # return dfs(0, target)
















    #     if sum(nums) % 2:
    #         return False

    #     target = sum(nums) // 2

    #     return self.dfs(0, nums, target)

    # def dfs(self, i, nums, target):
    #     if target == 0:
    #         return True


    #     if target < 0 or i >=len(nums):
    #         return False

    #     return self.dfs(i + 1, nums, target) or self.dfs(i + 1, nums, target - nums[i])

    


        