class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # BRUTE FORCE APPROACH
        def bruteForce(r, c):
            if r == m or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            
            return (bruteForce(r + 1, c) + bruteForce(r, c + 1))

        return bruteForce(0, 0)
        