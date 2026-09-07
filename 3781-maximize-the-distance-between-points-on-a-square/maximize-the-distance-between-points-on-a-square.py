class Solution:
    def maxDistance(self, side, points, k):
        P = 4 * side

        # Convert boundary points to positions on perimeter.
        a = []

        for x, y in points:
            if y == 0:
                pos = x
            elif x == side:
                pos = side + y
            elif y == side:
                pos = 3 * side - x
            else:
                pos = 4 * side - y

            a.append(pos)

        a.sort()
        n = len(a)

        # Duplicate the array to handle circular wrapping.
        b = a + [x + P for x in a]

        def can(d):
            # next[i] = first position >= b[i] + d
            # We calculate it with two pointers.
            nxt = [0] * (2 * n)
            j = 0

            for i in range(2 * n):
                if j < i + 1:
                    j = i + 1

                while j < 2 * n and b[j] - b[i] < d:
                    j += 1

                nxt[i] = j

            # Try every possible first point.
            # Binary lifting lets us jump k-1 times.
            LOG = k.bit_length()

            jump = [nxt]

            for p in range(1, LOG):
                prev = jump[-1]
                cur = [0] * (2 * n)

                for i in range(2 * n):
                    x = prev[i]
                    cur[i] = prev[x] if x < 2 * n else x

                jump.append(cur)

            for start in range(n):
                idx = start

                steps = k - 1
                bit = 0

                while steps:
                    if steps & 1:
                        idx = jump[bit][idx]

                    if idx >= start + n:
                        break

                    steps >>= 1
                    bit += 1

                if idx < start + n:
                    # Check circular distance from last to first.
                    if b[idx] - b[start] <= P - d:
                        return True

            return False

        low = 0
        high = 2 * side

        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high