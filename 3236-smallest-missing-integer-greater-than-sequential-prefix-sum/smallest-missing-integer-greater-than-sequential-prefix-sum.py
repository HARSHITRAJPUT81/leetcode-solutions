class Solution:
    def missingInteger(self, nums):
        # Find the longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Put all elements into a set for O(1) average lookup
        present = set(nums)

        # Find smallest missing integer >= total
        while total in present:
            total += 1

        return total