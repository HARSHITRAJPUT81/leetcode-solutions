class Solution:
    def rotateGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        # Process every layer
        layers = min(m, n) // 2

        for layer in range(layers):

            elements = []

            top = layer
            bottom = m - layer - 1
            left = layer
            right = n - layer - 1

            # Top row: left -> right
            for j in range(left, right + 1):
                elements.append(grid[top][j])

            # Right column: top+1 -> bottom
            for i in range(top + 1, bottom + 1):
                elements.append(grid[i][right])

            # Bottom row: right-1 -> left
            for j in range(right - 1, left - 1, -1):
                elements.append(grid[bottom][j])

            # Left column: bottom-1 -> top+1
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])

            # Effective rotation
            k2 = k % len(elements)

            # Counter-clockwise rotation
            elements = elements[k2:] + elements[:k2]

            index = 0

            # Put back into top row
            for j in range(left, right + 1):
                grid[top][j] = elements[index]
                index += 1

            # Put back into right column
            for i in range(top + 1, bottom + 1):
                grid[i][right] = elements[index]
                index += 1

            # Put back into bottom row
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = elements[index]
                index += 1

            # Put back into left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = elements[index]
                index += 1

        return grid