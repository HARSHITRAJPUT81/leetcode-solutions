class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Sort numbers along with their original indices
        arr = sorted((num, i) for i, num in enumerate(nums))

        result = [0] * n
        i = 0

        while i < n:
            j = i + 1

            # Find a connected group
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            # Get original indices and sorted values in this group
            indices = sorted(arr[k][1] for k in range(i, j))
            values = [arr[k][0] for k in range(i, j)]

            # Assign smallest values to smallest indices
            for idx, val in zip(indices, values):
                result[idx] = val

            i = j

        return result