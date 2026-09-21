class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with only num
            rem = num % k
            new_dp[rem] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_rem = (r * rem) % k
                    new_dp[new_rem] += dp[r]

            # Add all subarrays ending at current position
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans