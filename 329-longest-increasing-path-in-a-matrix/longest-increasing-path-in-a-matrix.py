class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]

            best = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and
                    0 <= nc < n and
                    matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))

            dp[r][c] = best
            return best

        ans = 0

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans
        