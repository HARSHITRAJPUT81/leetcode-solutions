class Solution:
    def canMakeEqual(self, nums, k):
        def check(target):
            arr = nums[:]
            ops = 0

            for i in range(len(arr) - 1):
                if arr[i] != target:
                    arr[i] *= -1
                    arr[i + 1] *= -1
                    ops += 1

            return arr[-1] == target and ops <= k

        return check(1) or check(-1)