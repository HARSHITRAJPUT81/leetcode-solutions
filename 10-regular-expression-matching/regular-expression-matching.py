class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)

        # Create DP table
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(2, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill DP table
        for i in range(1, n + 1):

            for j in range(1, m + 1):

                # Normal character match or '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':

                    dp[i][j] = dp[i - 1][j - 1]

                # Handle '*'
                elif p[j - 1] == '*':

                    # Zero occurrence
                    dp[i][j] = dp[i][j - 2]

                    # One or more occurrence
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[n][m]
        