class Solution:
    def maxNumber(self, nums1, nums2, k):
        def pick(nums, k):
            drop = len(nums) - k
            stack = []

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:k]

        def merge(a, b):
            ans = []

            while a or b:
                if a > b:
                    ans.append(a.pop(0))
                else:
                    ans.append(b.pop(0))

            return ans

        best = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for x in range(start, end + 1):
            a = pick(nums1, x)
            b = pick(nums2, k - x)

            candidate = merge(a[:], b[:])

            if candidate > best:
                best = candidate

        return best