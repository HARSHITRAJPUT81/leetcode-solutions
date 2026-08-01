from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):

        graph = defaultdict(list)

        # Build graph
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))

        def dfs(src, dest, visited):
            if src == dest:
                return 1.0

            visited.add(src)

            for nei, weight in graph[src]:
                if nei not in visited:
                    res = dfs(nei, dest, visited)
                    if res != -1:
                        return weight * res

            return -1

        ans = []

        for src, dest in queries:

            if src not in graph or dest not in graph:
                ans.append(-1.0)

            elif src == dest:
                ans.append(1.0)

            else:
                ans.append(dfs(src, dest, set()))

        return ans