class Solution:
    def longestCommonSubpath(self, n, paths):
        MOD = (1 << 61) - 1
        BASE = 100007

        minLen = min(len(p) for p in paths)

        powBase = [1] * (minLen + 1)
        for i in range(1, minLen + 1):
            powBase[i] = (powBase[i - 1] * BASE) % MOD

        def check(length):
            common = None

            for path in paths:
                if len(path) < length:
                    return False

                h = 0

                seen = set()

                for i in range(length):
                    h = (h * BASE + path[i] + 1) % MOD

                seen.add(h)

                for i in range(length, len(path)):
                    h = (
                        h * BASE
                        - (path[i - length] + 1) * powBase[length]
                        + path[i] + 1
                    ) % MOD

                    seen.add(h)

                if common is None:
                    common = seen
                else:
                    common &= seen

                if not common:
                    return False

            return True

        lo = 0
        hi = minLen

        while lo < hi:
            mid = (lo + hi + 1) // 2

            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo