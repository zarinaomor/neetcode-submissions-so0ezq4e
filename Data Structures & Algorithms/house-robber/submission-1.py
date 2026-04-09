class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


















        
        # rob1, rob2 = 0, 0

        # for n in nums:
        #     tmp = max(n + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = tmp
        # return rob2


        # for i in range(1, len(nums)):
        #     if i == 1:
        #         nums[i] = max(nums[i], nums[i - 1])
        #     else:
        #         nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        # return nums[-1]