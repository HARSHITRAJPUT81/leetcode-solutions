from math import gcd

class Solution:
    def gcdSum(self, nums):
        n = len(nums)

        prefixGcd = []
        mx = 0

        # Step 1: Construct prefixGcd
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))

        # Step 2: Sort the array
        prefixGcd.sort()

        # Step 3: Pair smallest with largest
        left = 0
        right = n - 1

        ans = 0

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans