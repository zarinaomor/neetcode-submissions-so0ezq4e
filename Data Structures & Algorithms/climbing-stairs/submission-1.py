class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        cache = {}

        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in cache:
            return cache[n]
        cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return cache[n]


        # BRUTE FORCE, Recursive approach
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)