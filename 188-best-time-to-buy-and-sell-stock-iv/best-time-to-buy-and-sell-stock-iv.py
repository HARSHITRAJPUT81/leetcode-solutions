class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, buy, cap):
            if i == n or cap == 0:
                return 0

            if buy:
                return max(
                    -prices[i] + dfs(i + 1, 0, cap),
                    dfs(i + 1, 1, cap)
                )
            else:
                return max(
                    prices[i] + dfs(i + 1, 1, cap - 1),
                    dfs(i + 1, 0, cap)
                )

        return dfs(0, 1, k)