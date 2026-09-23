class Solution:
    def minOperations(self, nums, x):
        n = len(nums)
        target = sum(nums) - x

        # If target is negative, impossible
        if target < 0:
            return -1

        # If target is 0, remove everything
        if target == 0:
            return n

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(n):
            curr_sum += nums[right]

            # Shrink window if sum becomes too large
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            # Found a subarray with required sum
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return n - max_len