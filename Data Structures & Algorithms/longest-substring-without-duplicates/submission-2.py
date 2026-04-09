class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0

        for r in range(l, len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


















        # BRUTE FORCE SOLUTION
        # res = 0
        # for i in range(len(s)):
        #     charSet = set()
        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     res = max(res, len(charSet))
        # return res




















        # length = 0
        # L = 0
        # window = set()

        # for R in range(len(s)):
        #     while s[R] in window:
        #         window.remove(s[L])
        #         L += 1
        #     window.add(s[R])
        #     length = max(R - L + 1, length)
        # return length

        
                
