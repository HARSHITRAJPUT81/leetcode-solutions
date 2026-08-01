class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)

        totalSum = sum(nums)

        curr = 0
        for i in range(n):
            curr += i * nums[i]

        ans = curr

        for i in range(1, n):
            curr = curr + totalSum - n * nums[n - i]
            ans = max(ans, curr)

        return ans