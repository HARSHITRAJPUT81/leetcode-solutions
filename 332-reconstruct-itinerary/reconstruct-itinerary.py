from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        # Build graph with min-heaps
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        ans = []

        def dfs(airport):
            while graph[airport]:
                nxt = heapq.heappop(graph[airport])
                dfs(nxt)
            ans.append(airport)

        dfs("JFK")

        return ans[::-1]