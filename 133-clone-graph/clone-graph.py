"""
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(curr):
            # Already cloned
            if curr in visited:
                return visited[curr]

            # Create clone
            clone = Node(curr.val)
            visited[curr] = clone

            # Clone neighbors
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)