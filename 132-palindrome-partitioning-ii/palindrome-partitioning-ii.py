class Solution:
    def minCut(self, s):
        n = len(s)

        # palindrome table
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = minimum cuts for s[0:i+1]
        dp = [0] * n

        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(i):
                    if pal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]
