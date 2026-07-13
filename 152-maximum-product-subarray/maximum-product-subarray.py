class Solution:
    def maxProduct(self, nums):
        maxProd = minProd = ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                maxProd, minProd = minProd, maxProd

            maxProd = max(num, maxProd * num)
            minProd = min(num, minProd * num)

            ans = max(ans, maxProd)

        return ans