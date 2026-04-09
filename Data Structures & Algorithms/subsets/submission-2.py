class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(i, subset):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # deciosion to include
            subset.append(nums[i])
            helper(i + 1, subset)
            # clean up the backtracking and decision NOT to include
            subset.pop()

            helper(i + 1, subset)
        
        helper(0, [])

        return res




















        # res = []

        # def helper(i, subset):
        #     # base case 
        #     if i >= len(nums):
        #         res.append(subset.copy())
        #         return
            
        #     # 1st decision to include nums[i]
        #     subset.append(nums[i])
        #     helper(i + 1, subset)

        #     # 2nd decision NOT to include nums[i]
        #     subset.pop()
        #     helper(i + 1, subset)

        # helper(0, [])

        # return res