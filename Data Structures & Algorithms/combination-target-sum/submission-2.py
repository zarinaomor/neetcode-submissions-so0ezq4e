class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sublist = []

        def helper(i, total):
            if total == target:
                res.append(sublist.copy())
                return

            if i >= len(nums) or total > target:
                return

            sublist.append(nums[i])
            helper(i, total + nums[i])
            sublist.pop()
            helper(i + 1, total)

        helper(0, 0)

        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = []

        # def helper(i, curComb, total):
        #     if total == target:
        #         res.append(curComb.copy())
        #         return

        #     if total > target or i >= len(nums):
        #         return

        #     curComb.append(nums[i])
        #     helper(i, curComb, total + nums[i])
        #     curComb.pop()

        #     helper(i + 1, curComb, total)
    

        # helper(0, [], 0)

        # return res
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # # res = []

        # # def helper(i, subset, total):
        # #     if total == target:
        # #         res.append(subset.copy())
        # #         return
            
        # #     if i >= len(nums) or total > target:
        # #         return

        # #     # decision to include nums[i]
        # #     subset.append(nums[i])
        # #     helper(i, subset, total + nums[i])
        # #     #  2nd decision NOT to include nums[i]
        # #     subset.pop()
        # #     helper(i + 1, subset, total)

        # # helper(0, [], 0)

        # # return res

