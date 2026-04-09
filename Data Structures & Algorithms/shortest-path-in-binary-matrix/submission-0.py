class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid: 
            return -1
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        if grid[n - 1][n - 1] == 1:
            return -1
        q = deque()
        visit = set()
        q.append([0, 0])
        visit.add((0, 0))

        length = 1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return length

                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr >= n or c + dc >= n or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visit:
                        continue
                    q.append([r + dr, c + dc])
                    visit.add((r + dr, c + dc))
            length += 1
        return -1
                