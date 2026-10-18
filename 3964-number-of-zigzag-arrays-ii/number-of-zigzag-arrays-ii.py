class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m
        if m == 1:
            return 0

        size = 2 * m

        # State:
        # First m entries: arrays whose last step is increasing
        # Next m entries: arrays whose last step is decreasing

        # Initialize DP for arrays of length 2.
        v = [0] * size

        for j in range(m):
            v[j] = j
            v[m + j] = m - 1 - j

        # Transition matrix.
        # New increasing count at j = sum of previous decreasing
        # counts at all values i < j.
        # New decreasing count at j = sum of previous increasing
        # counts at all values i > j.
        T = [[0] * size for _ in range(size)]

        for j in range(m):
            for i in range(j):
                T[j][m + i] = 1
            for i in range(j + 1, m):
                T[m + j][i] = 1

        def multiply(A, B):
            d = len(A)
            C = [[0] * d for _ in range(d)]

            for i in range(d):
                ci = C[i]
                ai = A[i]

                for k in range(d):
                    a = ai[k]
                    if a == 0:
                        continue

                    bk = B[k]
                    for j in range(d):
                        if bk[j]:
                            ci[j] += a * bk[j]

                for j in range(d):
                    ci[j] %= MOD

            return C

        def matrix_vector(A, vec):
            d = len(A)
            result = [0] * d

            for i in range(d):
                total = 0
                row = A[i]

                for j in range(d):
                    total += row[j] * vec[j]

                result[i] = total % MOD

            return result

        # We already have the counts for length 2.
        # Apply the transition matrix n - 2 times.
        power = n - 2

        while power:
            if power & 1:
                v = matrix_vector(T, v)

            power >>= 1

            if power:
                T = multiply(T, T)

        return sum(v) % MOD