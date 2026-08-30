class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Case 1: Both removed from the front
        front = right + 1

        # Case 2: Both removed from the back
        back = n - left

        # Case 3: One from front, one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)