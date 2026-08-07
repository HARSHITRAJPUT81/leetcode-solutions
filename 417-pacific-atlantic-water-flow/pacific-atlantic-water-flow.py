class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < m and
                    0 <= nc < n and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        # Pacific
        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)

        ans = []

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans