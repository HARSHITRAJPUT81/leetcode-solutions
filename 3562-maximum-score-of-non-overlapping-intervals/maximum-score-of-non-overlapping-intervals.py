from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Sort by left endpoint
        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )

        starts = [x[0] for x in arr]

        # next[i] = first interval whose left > current right
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        @lru_cache(None)
        def dp(i, count):
            # At most 4 intervals
            if i >= n or count == 0:
                return (0, ())

            # Option 1: skip this interval
            score1, indices1 = dp(i + 1, count)

            # Option 2: take this interval
            l, r, w, original_index = arr[i]

            score2, indices2 = dp(nxt[i], count - 1)

            score2 += w
            indices2 = tuple(sorted((original_index,) + indices2))

            # Choose the better option
            if score2 > score1:
                return (score2, indices2)

            if score2 < score1:
                return (score1, indices1)

            # Same score -> lexicographically smaller indices
            if indices2 < indices1:
                return (score2, indices2)

            return (score1, indices1)

        return list(dp(0, 4)[1])