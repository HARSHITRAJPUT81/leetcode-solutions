class Solution:
    def missingNumber(self, nums):
        ans = len(nums)

        for i in range(len(nums)):
            ans ^= i
            ans ^= nums[i]

        return ans