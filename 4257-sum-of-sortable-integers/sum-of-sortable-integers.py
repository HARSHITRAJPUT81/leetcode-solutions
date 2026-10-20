
class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        target = sorted(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            possible = True

            for i in range(0, n, k):
                block = nums[i:i + k]

                # The block must contain the correct elements
                if sorted(block) != target[i:i + k]:
                    possible = False
                    break

                # Count descents in the circular block
                descents = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        descents += 1

                # More than one descent means it cannot
                # be sorted by a cyclic rotation
                if descents > 1:
                    possible = False
                    break

            if possible:
                ans += k

        return ans
