class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        # Total number of elements
        total = m * n

        # Avoid unnecessary full rotations
        k = k % total

        # Convert 2D grid into 1D array
        arr = []

        for row in grid:
            arr.extend(row)

        # Shift to the right
        arr = arr[-k:] + arr[:-k]

        # Convert back to 2D
        result = []

        for i in range(0, total, n):
            result.append(arr[i:i + n])

        return result