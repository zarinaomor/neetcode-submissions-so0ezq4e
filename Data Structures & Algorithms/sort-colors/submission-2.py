class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        sorted_arr = sorted(count.keys())

        i = 0
        for n in sorted_arr:
            for j in range(count[n]):
                nums[i] = n
                i += 1
        return nums
        

        