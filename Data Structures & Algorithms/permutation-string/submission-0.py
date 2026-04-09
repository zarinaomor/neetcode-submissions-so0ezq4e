class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # SLIDING WINDOW
        if len(s1) > len(s2):
            return False
        
        countS1 = {}
        countS2 = {}

        for c in s1:
            countS1[c] = countS1.get(c, 0) + 1

        l = 0
        for r in range(l, len(s2)):
            countS2[s2[r]] = countS2.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                countS2[s2[l]] -= 1
                if countS2[s2[l]] == 0:
                    del countS2[s2[l]]
                l += 1

            if countS1 == countS2:
                return True
        return False
        



        # BRUTE FORCE SOLUTION O(n^3 logn)
        # s1 = sorted(s1)

        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         subStr = s2[i:j+1]
        #         subStr = sorted(subStr)
        #         if subStr == s1:
        #             return True
        # return False

        