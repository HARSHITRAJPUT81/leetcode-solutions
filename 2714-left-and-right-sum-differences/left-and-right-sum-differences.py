class Solution:
    def leftRightDifference(self, nums):
        n = len(nums)

        total = sum(nums)
        left_sum = 0
        answer = []

        for i in range(n):
            # Sum of elements to the right
            right_sum = total - left_sum - nums[i]

            answer.append(abs(left_sum - right_sum))

            # Add current element for next index
            left_sum += nums[i]

        return answer