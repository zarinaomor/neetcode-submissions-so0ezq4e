class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) solution. Kadane's algo
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum


        # brute force approach O(n^2)
        # maxSum = nums[0]
        # for i in range(len(nums)):
        #     curSum = 0
        #     for j in range(i, len(nums)):
        #         curSum += nums[j]
        #         maxSum = max(curSum, maxSum)
        # return maxSum

        