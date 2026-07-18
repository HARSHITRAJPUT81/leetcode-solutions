from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph and indegree array
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # Start with courses having no prerequisites
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []

        while q:
            node = q.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return order if len(order) == numCourses else []