class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each node:
        # [product of whole segment, counts of prefix products]
        size = 4 * n
        tree_prod = [1] * size
        tree_cnt = [[0] * k for _ in range(size)]

        def merge(node):
            left = node * 2
            right = left + 1

            # Product of the complete segment
            tree_prod[node] = (
                tree_prod[left] * tree_prod[right]
            ) % k

            cnt = [0] * k

            # Prefixes completely inside left segment
            for r in range(k):
                cnt[r] += tree_cnt[left][r]

            # Prefixes that use the complete left segment
            # and then a prefix of right segment
            p = tree_prod[left]

            for r in range(k):
                if tree_cnt[right][r]:
                    new_r = (p * r) % k
                    cnt[new_r] += tree_cnt[right][r]

            tree_cnt[node] = cnt

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k

                tree_prod[node] = rem
                tree_cnt[node][rem] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node)

        def update(node, l, r, idx, value):
            if l == r:
                rem = value % k

                tree_prod[node] = rem
                tree_cnt[node] = [0] * k
                tree_cnt[node][rem] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            merge(node)

        # Returns (product, prefix-count-array)
        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_cnt[node][:]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left_prod, left_cnt = query(
                node * 2, l, mid, ql, qr
            )

            right_prod, right_cnt = query(
                node * 2 + 1, mid + 1, r, ql, qr
            )

            # Merge the queried portions
            result_prod = (left_prod * right_prod) % k
            result_cnt = [0] * k

            # Prefixes completely in left part
            for x in range(k):
                result_cnt[x] += left_cnt[x]

            # Prefixes that contain all of left part
            for x in range(k):
                if right_cnt[x]:
                    new_x = (left_prod * x) % k
                    result_cnt[new_x] += right_cnt[x]

            return result_prod, result_cnt

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Update persists for future queries
            nums[index] = value
            update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            _, cnt = query(1, 0, n - 1, start, n - 1)

            answer.append(cnt[x])

        return answer