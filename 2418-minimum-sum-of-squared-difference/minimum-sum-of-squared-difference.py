class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        low, high = 0, max(diff)

        while low < high:
            mid = (low + high) // 2
            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                high = mid
            else:
                low = mid + 1

        limit = low
        operations = sum(max(0, d - limit) for d in diff)

        ans = sum(min(d, limit) ** 2 for d in diff)

        # Use any remaining operations to reduce differences
        remaining = k - operations

        for d in diff:
            if d > limit:
                ans += 0  # Already accounted for by the capped sum

        # Each remaining operation reduces one difference from limit to limit - 1
        count = sum(1 for d in diff if d >= limit and d > 0)
        remaining = min(remaining, count)

        return ans - remaining * (2 * limit - 1)