class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Start of a new sequence
            if num - 1 not in numSet:
                current = num
                length = 1

                while current + 1 in numSet:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest