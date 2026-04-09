class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        return self.dfs(0, nums, target)

    def dfs(self, i,nums, target):
        if i >= len(nums):
            return target == 0

        if target < 0:
            return False

        return self.dfs(i + 1, nums, target) or self.dfs(i + 1, nums, target - nums[i])

    


        