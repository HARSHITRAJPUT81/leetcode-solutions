class Solution:
    def minScore(self, n, roads):
        graph = [[] for _ in range(n + 1)]

        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        visited = [False] * (n + 1)
        visited[1] = True

        stack = [1]
        answer = float('inf')

        while stack:
            city = stack.pop()

            for next_city, distance in graph[city]:
                answer = min(answer, distance)

                if not visited[next_city]:
                    visited[next_city] = True
                    stack.append(next_city)

        return answer