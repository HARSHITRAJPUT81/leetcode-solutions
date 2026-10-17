class Solution:
    def minSwaps(self, nums):
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {val: i for i, val in enumerate(nums)}
        swaps = 0

        for i in range(len(nums)):
            if nums[i] != arr[i]:
                j = pos[arr[i]]

                pos[nums[i]] = j
                pos[arr[i]] = i

                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1

        return swaps