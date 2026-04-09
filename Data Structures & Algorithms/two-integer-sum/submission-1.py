class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i



















        # hashMap = {}

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hashMap:
        #         return [hashMap[diff], i]
        #     hashMap[n] = i


















        # hashMap = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hashMap:
        #         return [hashMap[diff], i]
        #     hashMap[n] = i


        # BRUTE FORCE approack O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return None



                
        