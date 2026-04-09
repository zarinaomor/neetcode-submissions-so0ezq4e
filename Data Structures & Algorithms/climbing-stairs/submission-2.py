class Solution:
    def climbStairs(self, n: int) -> int:
        # DP Bottom Up approach
        if n <= 2:
            return n
        table = [0] * (n + 1)
        table[1] = 1
        table[2] = 2

        for i in range(3, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        return table[n]





        # DP Top-Bottom approach
        # cache = {}

        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # if n in cache:
        #     return cache[n]
        # cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # return cache[n]


        # BRUTE FORCE, Recursive approach
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)