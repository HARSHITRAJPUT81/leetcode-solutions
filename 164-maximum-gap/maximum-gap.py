from math import ceil

class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        bucket_size = ceil((mx - mn) / (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - mn) // bucket_size

            if buckets[idx][0] is None:
                buckets[idx][0] = num
                buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        ans = 0
        prev_max = buckets[0][1]

        for i in range(1, bucket_count):
            if buckets[i][0] is None:
                continue

            ans = max(ans, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]

        return ans