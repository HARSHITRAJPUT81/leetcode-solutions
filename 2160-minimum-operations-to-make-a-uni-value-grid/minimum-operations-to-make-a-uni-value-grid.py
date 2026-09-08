class Solution:
    def minOperations(self, grid, x):
        # Flatten the grid
        arr = []

        for row in grid:
            for value in row:
                arr.append(value)

        # Check if all values have the same remainder
        remainder = arr[0] % x

        for value in arr:
            if value % x != remainder:
                return -1

        # Sort the values
        arr.sort()

        # Median
        median = arr[len(arr) // 2]

        # Calculate operations
        operations = 0

        for value in arr:
            operations += abs(value - median) // x

        return operations