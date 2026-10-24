from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        req = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i, p in enumerate(primes):
            while t % p == 0:
                req[i] += 1
                t //= p

        if t != 1:
            return "-1"

        # Prime factor contributions of digits 1 to 9
        factors = [
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        ]

        @lru_cache(None)
        def min_digits(a, b, c, d):
            if a == b == c == d == 0:
                return 0

            ans = float('inf')

            for x in range(1, 10):
                f = factors[x - 1]
                na = max(0, a - f[0])
                nb = max(0, b - f[1])
                nc = max(0, c - f[2])
                nd = max(0, d - f[3])

                if (na, nb, nc, nd) != (a, b, c, d):
                    ans = min(
                        ans,
                        1 + min_digits(na, nb, nc, nd)
                    )

            return ans

        def subtract(rem, digit):
            f = factors[digit - 1]
            return tuple(max(0, rem[i] - f[i]) for i in range(4))

        def build(rem, length):
            if min_digits(*rem) > length:
                return None

            result = []

            for pos in range(length):
                for digit in range(1, 10):
                    nr = subtract(rem, digit)

                    if min_digits(*nr) <= length - pos - 1:
                        result.append(str(digit))
                        rem = nr
                        break

            return ''.join(result)

        # Prefix factor counts
        n = len(num)
        pref = [[0] * 4 for _ in range(n + 1)]
        first_zero = n

        for i, ch in enumerate(num):
            pref[i + 1] = pref[i].copy()

            if ch == '0':
                first_zero = min(first_zero, i)
                continue

            f = factors[int(ch) - 1]

            for j in range(4):
                pref[i + 1][j] = min(
                    req[j], pref[i][j] + f[j]
                )

        # If num itself is valid, return it
        if first_zero == n:
            rem = tuple(
                max(0, req[j] - pref[n][j])
                for j in range(4)
            )

            if rem == (0, 0, 0, 0):
                return num

        # Try increasing one digit, from right to left
        for i in range(n - 1, -1, -1):
            if i > first_zero:
                continue

            base = tuple(
                max(0, req[j] - pref[i][j])
                for j in range(4)
            )

            start = max(1, int(num[i]) + 1)

            for digit in range(start, 10):
                rem = subtract(base, digit)
                suffix_len = n - i - 1

                if min_digits(*rem) <= suffix_len:
                    suffix = build(rem, suffix_len)

                    return num[:i] + str(digit) + suffix

        # No answer of the same length; use a longer number
        length = max(n + 1, min_digits(*req))
        return build(tuple(req), length)