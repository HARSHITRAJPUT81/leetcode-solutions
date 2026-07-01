class Solution:
    def totalNQueens(self, n: int) -> int:

        def dfs(cols, diag1, diag2):
            if cols == (1 << n) - 1:
                return 1

            count = 0
            available = ~ (cols | diag1 | diag2) & ((1 << n) - 1)

            while available:
                pos = available & -available
                available -= pos

                count += dfs(
                    cols | pos,
                    (diag1 | pos) << 1,
                    (diag2 | pos) >> 1
                )

            return count

        return dfs(0, 0, 0)