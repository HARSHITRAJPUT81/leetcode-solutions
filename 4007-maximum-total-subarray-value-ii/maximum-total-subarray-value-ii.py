import heapq

class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        # ---------- Sparse Table ----------
        LOG = n.bit_length()

        mx = [[0] * LOG for _ in range(n)]
        mn = [[0] * LOG for _ in range(n)]

        # Length = 1
        for i in range(n):
            mx[i][0] = nums[i]
            mn[i][0] = nums[i]

        # Build sparse table
        for j in range(1, LOG):
            length = 1 << j
            half = length >> 1

            for i in range(n - length + 1):
                mx[i][j] = max(
                    mx[i][j - 1],
                    mx[i + half][j - 1]
                )

                mn[i][j] = min(
                    mn[i][j - 1],
                    mn[i + half][j - 1]
                )

        # Precompute logarithms
        log = [0] * (n + 1)

        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1

        # ---------- Range Value ----------
        def value(l, r):
            length = r - l + 1
            j = log[length]

            maximum = max(
                mx[l][j],
                mx[r - (1 << j) + 1][j]
            )

            minimum = min(
                mn[l][j],
                mn[r - (1 << j) + 1][j]
            )

            return maximum - minimum

        # ---------- Max Heap ----------
        # Python has a min heap, so store negative values.
        heap = []

        # For every l, start with [l, n-1]
        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        # Pick the largest k subarrays
        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)

            v = -neg_v
            ans += v

            # Move to the previous subarray
            # having the same left endpoint.
            if r > l:
                new_r = r - 1
                new_v = value(l, new_r)

                heapq.heappush(
                    heap,
                    (-new_v, l, new_r)
                )

        return ans