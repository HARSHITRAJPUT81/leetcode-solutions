class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        from functools import lru_cache

        def solve(n):
            if n < 100:
                return 0

            digits = list(map(int, str(n)))

            @lru_cache(None)
            def dp(pos, prev2, prev1, tight, started):
                if pos == len(digits):
                    return (1, 0)

                limit = digits[pos] if tight else 9

                count = 0
                total = 0

                for d in range(limit + 1):
                    ntight = tight and (d == digits[pos])

                    # Leading zeros
                    if not started and d == 0:
                        c, w = dp(
                            pos + 1,
                            -1,
                            -1,
                            ntight,
                            False
                        )

                        count += c
                        total += w
                        continue

                    # First digit
                    if not started:
                        c, w = dp(
                            pos + 1,
                            -1,
                            d,
                            ntight,
                            True
                        )

                        count += c
                        total += w
                        continue

                    # We now have prev2, prev1, d
                    add = 0

                    if prev2 != -1:
                        if (prev1 > prev2 and prev1 > d) or \
                           (prev1 < prev2 and prev1 < d):
                            add = 1

                    c, w = dp(
                        pos + 1,
                        prev1,
                        d,
                        ntight,
                        True
                    )

                    count += c

                    # Every continuation gets the contribution
                    # of prev1 being a peak/valley.
                    total += w + c * add

                return count, total

            return dp(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)