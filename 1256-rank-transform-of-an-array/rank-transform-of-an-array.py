class Solution:
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(set(arr))

        rank = {}

        for i, value in enumerate(sorted_unique, 1):
            rank[value] = i

        return [rank[x] for x in arr]