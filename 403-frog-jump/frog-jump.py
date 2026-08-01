from functools import lru_cache

class Solution:
    def canCross(self, stones):
        stone_set = set(stones)
        last = stones[-1]

        @lru_cache(None)
        def dfs(position, jump):
            if position == last:
                return True

            for step in (jump - 1, jump, jump + 1):
                if step > 0 and (position + step) in stone_set:
                    if dfs(position + step, step):
                        return True

            return False

        return dfs(0, 0)