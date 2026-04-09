class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest




















        # BRUTE FORCE SOLUTION O(nlogn)
        # sortedNum = sorted(nums)
        # longest = 1
        # current = 1

        # for i in range(1, len(sortedNum)):
        #     if sortedNum[i] == sortedNum[i - 1] + 1:
        #         current += 1
        #     elif sortedNum[i] != sortedNum[i - 1]:
        #         longest = max(longest, current)
        #         current = 1

        # return max(longest, current)
            
                

        