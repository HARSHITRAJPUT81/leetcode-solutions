class Solution:
    def maximumProduct(self, nums):
        nums.sort()

        n = len(nums)

        # Case 1: three largest
        product1 = nums[n - 1] * nums[n - 2] * nums[n - 3]

        # Case 2: two smallest + largest
        product2 = nums[0] * nums[1] * nums[n - 1]

        return max(product1, product2)