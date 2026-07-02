class Solution:
    def insert(self, intervals, newInterval):

        ans = []

        start, end = newInterval

        for s, e in intervals:

            # interval completely before newInterval
            if e < start:
                ans.append([s, e])

            # interval completely after newInterval
            elif s > end:
                ans.append([start, end])
                start, end = s, e

            # overlapping intervals
            else:
                start = min(start, s)
                end = max(end, e)

        ans.append([start, end])

        return ans