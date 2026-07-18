class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []

        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                return

            if total > n:
                return

            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()

        backtrack(1, [], 0)
        return ans