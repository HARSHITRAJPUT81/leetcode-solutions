from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])

        # Iterate over the smaller dimension
        if m > n:
            matrix = list(zip(*matrix))
            m, n = n, m

        ans = float("-inf")

        for left in range(n):
            rowsum = [0] * m

            for right in range(left, n):

                for r in range(m):
                    rowsum[r] += matrix[r][right]

                prefix = 0
                prefixes = [0]

                for x in rowsum:
                    prefix += x

                    idx = bisect_left(prefixes, prefix - k)

                    if idx < len(prefixes):
                        ans = max(ans, prefix - prefixes[idx])

                    insort(prefixes, prefix)

        return ans