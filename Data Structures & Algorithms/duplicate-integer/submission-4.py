class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False





        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True

        # return False


















        # hashSet = set()

        # for n in nums:
        #     if n in hashSet:
        #         return True
        #     hashSet.add(n)
        # return False









        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False




        




















        # hashSet = set()
        
        # for n in nums:
        #     if n in hashSet:
        #         return True
        #     hashSet.add(n)
        # return False
        
         