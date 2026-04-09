class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l, total = 0, 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                cur_len = r - l + 1
                min_len = min(min_len, cur_len)
                total -= nums[l]
                l += 1
        return min_len if min_len != float('inf') else 0



        # brute force approach
        # min_len = float('inf')

        # for i in range(len(nums)):
        #     cur_sum = 0
            
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]
        #         if cur_sum >= target:
        #             cur_len = j - i + 1
        #             if cur_len < min_len:
        #                 min_len = cur_len
        #                 break

        # return min_len if min_len != float('inf') else 0