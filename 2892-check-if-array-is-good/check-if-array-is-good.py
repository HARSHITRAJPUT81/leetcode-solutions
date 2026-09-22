class Solution:
    def isGood(self, nums):
        n = max(nums)

        # Length must be n + 1
        if len(nums) != n + 1:
            return False

        # Check frequencies
        for i in range(1, n):
            if nums.count(i) != 1:
                return False

        # Maximum n must appear exactly twice
        if nums.count(n) != 2:
            return False

        return True