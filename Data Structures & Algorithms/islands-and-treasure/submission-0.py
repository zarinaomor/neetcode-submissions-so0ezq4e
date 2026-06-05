class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        INF = 2147483647
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))


        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr, nc) not in visit and 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    visit.add((nr, nc))
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))
                 



        
    