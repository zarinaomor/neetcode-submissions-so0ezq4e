class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom Up Approach 
        N, M = len(text1), len(text2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(N):
            for j in range(M):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[N][M]

   
   
   
   
   
   
   
    # Memoization. Top-Bottom approach. Caching
    #     n, m = len(text1), len(text2)
    #     cache = [[-1] * (m + 1) for _ in range(n)]
    #     return self.helper(text1, text2, 0, 0, cache)

    # def helper(self, text1, text2, i1, i2, cache):
    #     if i1 == len(text1) or i2 == len(text2):
    #         return 0

    #     if cache[i1][i2] != -1:
    #         return cache[i1][i2]

    #     if text1[i1] == text2[i2]:
    #         cache[i1][i2] = 1 + self.helper(text1, text2, i1 + 1, i2 + 1, cache)
    #     else:
    #         cache[i1][i2] = max(self.helper(text1, text2, i1 + 1, i2, cache),
    #                             self.helper(text1, text2, i1, i2 + 1, cache))

    #     return cache[i1][i2]



    
    
    
    
    
    
    
    
    
    # BRUTE FORCE
    #     return self.helper(text1, text2, 0, 0)

    # def helper(self, text1, text2, i1, i2):
    #     if i1 == len(text1) or i2 == len(text2):
    #         return 0

    #     if text1[i1] == text2[i2]:
    #         return 1 + self.helper(text1, text2, i1 + 1, i2+ 1)
    #     else:
    #         return max(self.helper(text1, text2, i1 + 1, i2),
    #                 self.helper(text1, text2, i1, i2 + 1))

    #     return 0