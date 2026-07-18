import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []

        # Add start and end events
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))

        events.sort()

        res = []
        heap = [(0, float('inf'))]   # (-height, right)

        for x, negH, r in events:

            # Remove expired buildings
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # Add new building
            if negH:
                heapq.heappush(heap, (negH, r))

            curr = -heap[0][0]

            if not res or res[-1][1] != curr:
                res.append([x, curr])

        return res