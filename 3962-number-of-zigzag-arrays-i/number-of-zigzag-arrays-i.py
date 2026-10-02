class Solution:
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1

        # For length 1, every value is valid
        up = [1] * m
        down = [1] * m

        for _ in range(2, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            # Prefix sum of down
            prefix = 0
            for i in range(m):
                new_up[i] = prefix
                prefix = (prefix + down[i]) % MOD

            # Suffix sum of up
            suffix = 0
            for i in range(m - 1, -1, -1):
                new_down[i] = suffix
                suffix = (suffix + up[i]) % MOD

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD