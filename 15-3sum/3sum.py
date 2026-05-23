class Solution:
    def threeSum(self, nums):

        # Sort the array
        nums.sort()

        answer = []

        # Loop through each number
        for i in range(len(nums)):

            # Skip duplicate numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            # Use two pointers
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # If sum is 0, save answer
                if total == 0:
                    answer.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                # If sum is smaller, move left pointer
                elif total < 0:
                    left += 1

                # If sum is bigger, move right pointer
                else:
                    right -= 1

        return answer
        