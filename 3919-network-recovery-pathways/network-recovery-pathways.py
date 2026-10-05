class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        # Build graph
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1

        # Topological sorting
        queue = []

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        topo = []

        while queue:
            u = queue.pop()
            topo.append(u)

            for v, cost in graph[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    queue.append(v)

        # Check if score x is possible
        def possible(x):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0

            for u in topo:

                if dist[u] == INF:
                    continue

                # Intermediate node must be online
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, cost in graph[u]:

                    # Edge cost must be at least x
                    if cost < x:
                        continue

                    # Destination intermediate node must be online
                    if v != n - 1 and not online[v]:
                        continue

                    new_cost = dist[u] + cost

                    if new_cost <= k and new_cost < dist[v]:
                        dist[v] = new_cost

            return dist[n - 1] <= k

        # Binary search for maximum minimum edge cost
        low = 0
        high = max((cost for _, _, cost in edges), default=0)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans