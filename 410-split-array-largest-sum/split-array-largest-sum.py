class Solution:
    def splitArray(self, nums, k):
        def canSplit(maxSum):
            count = 1
            curr = 0

            for num in nums:
                if curr + num > maxSum:
                    count += 1
                    curr = num
                else:
                    curr += num

            return count <= k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left