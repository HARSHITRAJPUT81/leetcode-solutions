class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i...j] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 2 or pal[i + 1][j - 1]:
                        pal[i][j] = True

        # dp[i] = maximum number of palindromes
        # using characters s[0...i-1]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't use a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Try every possible starting position
            for start in range(i - k + 1):
                if pal[start][i - 1]:
                    # Length must be at least k
                    dp[i] = max(dp[i], dp[start] + 1)

        return dp[n]