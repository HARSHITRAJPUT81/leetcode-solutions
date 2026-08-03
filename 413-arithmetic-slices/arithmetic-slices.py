class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)

        if n < 3:
            return 0

        ans = 0
        dp = 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
                ans += dp
            else:
                dp = 0

        return ans