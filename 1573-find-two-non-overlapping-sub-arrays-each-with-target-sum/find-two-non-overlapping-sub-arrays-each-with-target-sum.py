class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1

        # best[i] = shortest target-sum subarray
        # ending at or before index i
        best = [INF] * n

        left = 0
        curr_sum = 0
        shortest = INF
        ans = INF

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window if sum is too large
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Found a subarray [left, right]
            if curr_sum == target:
                length = right - left + 1

                # There must be a previous subarray
                # completely before 'left'
                if left > 0:
                    ans = min(ans, length + best[left - 1])

                shortest = min(shortest, length)

            best[right] = shortest

        return -1 if ans == INF else ans