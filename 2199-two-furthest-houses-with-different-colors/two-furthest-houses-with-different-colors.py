class Solution:
    def maxDistance(self, colors):
        n = len(colors)

        # From the left
        i = 0
        while i < n and colors[i] == colors[-1]:
            i += 1

        ans1 = n - 1 - i

        # From the right
        j = n - 1
        while j >= 0 and colors[j] == colors[0]:
            j -= 1

        ans2 = j

        return max(ans1, ans2)