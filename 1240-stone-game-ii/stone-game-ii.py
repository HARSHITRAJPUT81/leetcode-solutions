class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # Suffix sum
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            # All remaining stones can be taken
            if i >= n:
                return 0

            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                # Stones opponent can get afterward
                opponent = dp(i + X, max(M, X))

                # Current player gets total remaining
                # minus what opponent can get
                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)