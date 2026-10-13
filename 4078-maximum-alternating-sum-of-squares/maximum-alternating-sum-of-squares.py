class Solution:
    def maxAlternatingSum(self, nums):
        nums = sorted(x * x for x in nums)
        
        n = len(nums)
        k = n // 2
        
        return sum(nums[k:]) - sum(nums[:k])