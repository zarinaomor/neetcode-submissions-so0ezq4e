class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if (r - l + 1) - max(count.values()) <= k:
                res = max(res, (r - l + 1))
            else:
                count[s[l]] -= 1
                l += 1

        return res





















        # count = {}
        # res = 0
        # L = 0

        # for R in range(len(s)):
        #     count[s[R]] = 1 + count.get(s[R], 0)

        #     if (R - L + 1) - max(count.values()) > k:
        #         count[s[L]] -= 1
        #         L += 1
        #     res = max(R - L + 1, res)
    
        # return res       