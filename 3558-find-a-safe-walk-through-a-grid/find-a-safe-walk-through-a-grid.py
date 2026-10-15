from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])

        if health <= grid[0][0]:
            return False

        q = deque([(0, 0, health - grid[0][0])])
        best = [[0] * n for _ in range(m)]
        best[0][0] = health - grid[0][0]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, h = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            if h < best[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    nh = h - grid[nr][nc]

                    if nh > 0 and nh > best[nr][nc]:
                        best[nr][nc] = nh
                        q.append((nr, nc, nh))

        return False