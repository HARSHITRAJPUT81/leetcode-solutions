class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        ans = 0

        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            ans = max(ans, self.largestRectangleArea(heights))

        return ans

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        h = heights + [0]  # Sentinel

        for i in range(len(h)):
            while stack and h[stack[-1]] > h[i]:
                height = h[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area