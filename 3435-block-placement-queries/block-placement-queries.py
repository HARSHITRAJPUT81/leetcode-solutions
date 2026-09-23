class Solution:
    def getResults(self, queries):
        MAX = 50001

        # Fenwick Tree:
        # Used to know which positions contain obstacles
        bit = [0] * (MAX + 2)

        def add(pos, val):
            pos += 1
            while pos < len(bit):
                bit[pos] += val
                pos += pos & -pos

        def prefix(pos):
            pos += 1
            result = 0

            while pos > 0:
                result += bit[pos]
                pos -= pos & -pos

            return result

        def kth(k):
            """
            Return the position of the k-th obstacle.
            k is 1-based.
            """
            pos = 0
            step = 1 << 16

            while step:
                nxt = pos + step

                if nxt < len(bit) and bit[nxt] < k:
                    k -= bit[nxt]
                    pos = nxt

                step >>= 1

            return pos

        # Segment tree for maximum gap
        size = 1
        while size < MAX:
            size *= 2

        seg = [0] * (2 * size)

        def update(pos, value):
            pos += size
            seg[pos] = value

            pos //= 2

            while pos:
                seg[pos] = max(seg[pos * 2],
                               seg[pos * 2 + 1])
                pos //= 2

        def range_max(left, right):
            if left > right:
                return 0

            left += size
            right += size

            ans = 0

            while left <= right:
                if left % 2 == 1:
                    ans = max(ans, seg[left])
                    left += 1

                if right % 2 == 0:
                    ans = max(ans, seg[right])
                    right -= 1

                left //= 2
                right //= 2

            return ans

        # Initially obstacle at 0
        add(0, 1)

        # Gap ending at obstacle 0
        update(0, 0)

        results = []

        for q in queries:

            # ---------------------------------
            # Type 1: Add obstacle at x
            # ---------------------------------
            if q[0] == 1:
                x = q[1]

                # Number of obstacles <= x
                count_before = prefix(x - 1)

                # Previous obstacle
                prev = 0

                if count_before > 0:
                    prev = kth(count_before)

                # Number of obstacles <= x
                count_at_x = prefix(x)

                # Next obstacle
                total_obstacles = prefix(MAX - 1)

                nxt = MAX

                if count_at_x < total_obstacles:
                    nxt = kth(count_at_x + 1)

                # Add obstacle x
                add(x, 1)

                # Gap from previous obstacle to x
                update(x, x - prev)

                # If there is a next obstacle,
                # its previous obstacle has changed.
                if nxt != MAX:
                    update(nxt, nxt - x)

            # ---------------------------------
            # Type 2: Check block [2, x, sz]
            # ---------------------------------
            else:
                x = q[1]
                sz = q[2]

                # Find last obstacle <= x
                count = prefix(x)

                last = kth(count)

                # Free space after last obstacle
                end_gap = x - last

                # Maximum gap ending at an obstacle <= x
                best_gap = range_max(0, x)

                best_gap = max(best_gap, end_gap)

                results.append(best_gap >= sz)

        return results