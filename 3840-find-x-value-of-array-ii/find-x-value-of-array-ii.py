class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # tree[node] = number of prefix products for each remainder
        tree = [[0] * k for _ in range(4 * n)]

        # product[node] = product of the whole segment modulo k
        product = [1] * (4 * n)

        def merge(node, left, right):
            # Prefixes completely inside the left segment
            for r in range(k):
                tree[node][r] = tree[left][r]

            # Prefixes that go through the whole left segment
            # and then take a prefix of the right segment
            for r in range(k):
                new_r = (product[left] * r) % k
                tree[node][new_r] += tree[right][r]

            # Product of the complete segment
            product[node] = (product[left] * product[right]) % k

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k
                tree[node][rem] = 1
                product[node] = rem
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node, node * 2, node * 2 + 1)

        def update(node, l, r, index, value):
            if l == r:
                tree[node] = [0] * k

                rem = value % k
                tree[node][rem] = 1
                product[node] = rem
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            merge(node, node * 2, node * 2 + 1)

        def query(node, l, r, ql, qr):
            # Complete segment is inside query range
            if ql <= l and r <= qr:
                return tree[node][:], product[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left_cnt, left_product = query(
                node * 2, l, mid, ql, qr
            )

            right_cnt, right_product = query(
                node * 2 + 1, mid + 1, r, ql, qr
            )

            result_cnt = left_cnt[:]

            for rem in range(k):
                new_rem = (left_product * rem) % k
                result_cnt[new_rem] += right_cnt[rem]

            result_product = (left_product * right_product) % k

            return result_cnt, result_product

        # Build initial segment tree
        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Update persists for future queries
            update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            cnt, _ = query(1, 0, n - 1, start, n - 1)

            answer.append(cnt[x])

        return answer