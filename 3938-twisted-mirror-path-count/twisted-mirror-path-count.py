class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        m, n = len(grid), len(grid[0])

        # dpR: Ways entering a cell while moving right
        # dpD: Ways entering a cell while moving down
        dpR = [[0] * n for _ in range(m)]
        dpD = [[0] * n for _ in range(m)]

        dpR[0][0] = 1

        for i in range(m):
            for j in range(n):

                # Starting position
                if i == 0 and j == 0:
                    ways = 1
                else:
                    ways = (dpR[i][j] + dpD[i][j]) % MOD

                if ways == 0:
                    continue

                # If current cell is a mirror
                if grid[i][j] == 1 and (i != 0 or j != 0):

                    # Entered while moving right:
                    # Reflection sends robot down
                    if dpR[i][j]:
                        if i + 1 < m:
                            dpD[i + 1][j] = (
                                dpD[i + 1][j] + dpR[i][j]
                            ) % MOD

                    # Entered while moving down:
                    # Reflection sends robot right
                    if dpD[i][j]:
                        if j + 1 < n:
                            dpR[i][j + 1] = (
                                dpR[i][j + 1] + dpD[i][j]
                            ) % MOD

                else:
                    # Normal cell: move right
                    if j + 1 < n:
                        dpR[i][j + 1] = (
                            dpR[i][j + 1] + ways
                        ) % MOD

                    # Normal cell: move down
                    if i + 1 < m:
                        dpD[i + 1][j] = (
                            dpD[i + 1][j] + ways
                        ) % MOD

        return (dpR[m - 1][n - 1] +
                dpD[m - 1][n - 1]) % MOD