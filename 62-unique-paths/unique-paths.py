class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        N = m + n - 2
        r = min(m - 1, n - 1)

        ans = 1

        for i in range(1, r + 1):
            ans = ans * (N - r + i) // i

        return ans