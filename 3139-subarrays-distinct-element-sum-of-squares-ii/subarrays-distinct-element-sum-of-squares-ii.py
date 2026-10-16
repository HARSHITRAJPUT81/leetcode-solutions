class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        sums = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, length, v):
            tree[node] = (tree[node] + 2 * v * sums[node]
                          + v * v * length) % MOD
            sums[node] = (sums[node] + v * length) % MOD
            lazy[node] += v

        def push(node, start, end):
            if lazy[node]:
                mid = (start + end) // 2
                v = lazy[node]
                apply(node * 2, mid - start + 1, v)
                apply(node * 2 + 1, end - mid, v)
                lazy[node] = 0

        def update(node, start, end, left, right, v):
            if left > end or right < start:
                return

            if left <= start and end <= right:
                apply(node, end - start + 1, v)
                return

            push(node, start, end)
            mid = (start + end) // 2

            update(node * 2, start, mid, left, right, v)
            update(node * 2 + 1, mid + 1, end, left, right, v)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            sums[node] = (sums[node * 2] + sums[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            last[x] = i
            ans = (ans + tree[1]) % MOD

        return ans