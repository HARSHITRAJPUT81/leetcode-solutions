class Solution:
    def threeSumClosest(self, nums, target):

        # Sort the array
        nums.sort()

        # Take first three numbers as starting answer
        closest = nums[0] + nums[1] + nums[2]

        # Loop through the array
        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            # Use two pointers
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Update closest sum
                if abs(target - total) < abs(target - closest):
                    closest = total

                # If exact target found
                if total == target:
                    return total

                # Move left pointer
                elif total < target:
                    left += 1

                # Move right pointer
                else:
                    right -= 1

        return closest
        