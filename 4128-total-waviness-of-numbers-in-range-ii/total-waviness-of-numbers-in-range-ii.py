class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        from functools import lru_cache

        def solve(n):
            if n <= 0:
                return 0

            digits = list(map(int, str(n)))
            length = len(digits)

            @lru_cache(None)
            def dp(pos, prev2, prev1, started, tight):
                # pos == length -> no more digits
                if pos == length:
                    return (0, 1)

                limit = digits[pos] if tight else 9

                total_waviness = 0
                total_numbers = 0

                for d in range(limit + 1):
                    new_tight = tight and (d == limit)

                    # Still leading zeros
                    if not started and d == 0:
                        w, cnt = dp(
                            pos + 1,
                            -1,
                            -1,
                            False,
                            new_tight
                        )

                    else:
                        if not started:
                            # First real digit
                            w, cnt = dp(
                                pos + 1,
                                -1,
                                d,
                                True,
                                new_tight
                            )

                        else:
                            # We now have prev2, prev1 and current d.
                            add = 0

                            if prev2 != -1:
                                if prev1 > prev2 and prev1 > d:
                                    add = 1
                                elif prev1 < prev2 and prev1 < d:
                                    add = 1

                            w, cnt = dp(
                                pos + 1,
                                prev1,
                                d,
                                True,
                                new_tight
                            )

                            w += add * cnt

                    total_waviness += w
                    total_numbers += cnt

                return total_waviness, total_numbers

            return dp(0, -1, -1, False, True)[0]

        return solve(num2) - solve(num1 - 1)