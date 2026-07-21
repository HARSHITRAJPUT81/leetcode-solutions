class Solution:
    def numSquares(self, n: int) -> int:
        
        # dp[i] stores minimum squares needed for i
        dp = [float('inf')] * (n + 1)
        
        dp[0] = 0
        
        # Generate all perfect squares
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        # Fill dp array
        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]