class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, r, c, visit):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1):
                return 0
            # means we reached the end
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visit.add((r, c))

            count = 0
            # DFS DOWN
            count += dfs(grid, r + 1, c, visit)
            # DFS UP
            count += dfs(grid, r - 1, c, visit)
            # DFS RIGHT
            count += dfs(grid, r, c + 1, visit)
            # DFS LEFT
            count += dfs(grid, r, c - 1, visit)

            # clean up hash Set to do backtracking and see if other path exist
            visit.remove((r, c))
            return count

        return dfs(grid, 0, 0, set())
    





