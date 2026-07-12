class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if board[r][c] != 'O':
                return

            board[r][c] = '#'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # First and last column
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        # First and last row
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # Convert cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'