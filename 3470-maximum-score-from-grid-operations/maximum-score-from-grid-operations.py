class Solution:
    def maximumScore(self, grid):
        n = len(grid)

        # prefix[j][i] = sum of first i cells in column j
        prefix = [[0] * (n + 1) for _ in range(n)]

        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]

        # prevPick[i]:
        # maximum score up to previous column when the bottom
        # of the selected/black part is at i - 1.
        prevPick = [0] * (n + 1)

        # prevSkip[i]:
        # maximum score when the previous column itself is skipped
        # and the relevant boundary is from the column before it.
        prevSkip = [0] * (n + 1)

        for j in range(1, n):
            currPick = [0] * (n + 1)
            currSkip = [0] * (n + 1)

            for curr in range(n + 1):
                for prev in range(n + 1):

                    if curr > prev:
                        # Current column extends deeper.
                        #
                        # Rows [prev, curr) in the PREVIOUS column
                        # are white and adjacent to black cells.
                        score = (
                            prefix[j - 1][curr]
                            - prefix[j - 1][prev]
                        )

                        currPick[curr] = max(
                            currPick[curr],
                            prevSkip[prev] + score
                        )

                        currSkip[curr] = max(
                            currSkip[curr],
                            prevSkip[prev] + score
                        )

                    else:
                        # Previous column extends deeper.
                        #
                        # Rows [curr, prev) in CURRENT column
                        # are white and adjacent to black cells.
                        score = (
                            prefix[j][prev]
                            - prefix[j][curr]
                        )

                        currPick[curr] = max(
                            currPick[curr],
                            prevPick[prev] + score
                        )

                        currSkip[curr] = max(
                            currSkip[curr],
                            prevPick[prev]
                        )

            prevPick = currPick
            prevSkip = currSkip

        return max(prevPick)