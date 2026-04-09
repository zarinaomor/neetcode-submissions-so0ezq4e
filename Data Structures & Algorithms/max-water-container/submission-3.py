class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res


















        # BRUTE FORCE SOLUTION
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         # area = width * length
        #         area = (j - i) * min(heights[i], heights[j])
        #         res = max(res, area)
        # return res





















        # l = 0
        # r = len(heights) - 1
        # maxArea = 0

        # while l < r:
        #     area = min(heights[l], heights[r]) * (r - l)
        #     maxArea = max(maxArea, area)
        #     if heights[l] < heights[r]:
        #         l += 1
        #     elif heights[r] <= heights[l]:
        #         r -= 1
        # return maxArea