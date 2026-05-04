class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find a pivot (min number)
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        # smallest number
        pivot = l

        # Decide Right or Left portion
        if nums[pivot] <= target <= nums[-1]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot - 1
        
        # search target
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1




        