class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [[] for i in range(n)]
        postfix = [[] for i in range(n)]
        res = [0] * n
        
        prefix[0] = 1
        postfix[n - 1] = 1
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        for i in range(n):
            res[i] = prefix[i] * postfix[i]
        return res





       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # res = [1] * len(nums)

        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res