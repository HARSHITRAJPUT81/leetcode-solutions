from collections import deque

class Solution:
    def largestPathValue(self, colors, edges):
        n = len(colors)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        dp = [[0] * 26 for _ in range(n)]

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1

        processed = 0
        ans = 0

        while q:
            u = q.popleft()
            processed += 1

            ans = max(ans, max(dp[u]))

            for v in graph[u]:
                for c in range(26):
                    dp[v][c] = max(
                        dp[v][c],
                        dp[u][c] + (1 if c == ord(colors[v]) - ord('a') else 0)
                    )

                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        return ans if processed == n else -1