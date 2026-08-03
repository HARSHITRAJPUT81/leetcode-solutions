class Solution:
    def maxSumMinProduct(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Previous smaller
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # Next smaller
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        ans = 0

        for i in range(n):
            total = prefix[right[i]] - prefix[left[i] + 1]
            ans = max(ans, nums[i] * total)

        return ans % MOD