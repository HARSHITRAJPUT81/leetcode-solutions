from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque()

        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size

            for _ in range(size):
                leaf = leaves.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)