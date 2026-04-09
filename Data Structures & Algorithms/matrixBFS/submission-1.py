class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        q.append((0, 0))
        visit.add((0, 0))

        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr == ROWS or c + dc == COLS or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visit:
                        continue
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1

        return -1











        