class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            # decision to include nums[i]
            subset.append(nums[i])
            helper(i, subset, total + nums[i])
            #  2nd decision NOT to include nums[i]
            subset.pop()
            helper(i + 1, subset, total)

        helper(0, [], 0)

        return res

