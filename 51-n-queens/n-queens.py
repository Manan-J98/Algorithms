class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # create a matrix
        board = [(['.'] * n) for i in range(n)]
        res = []
        # recursive function
        def solve(row):
            # base case 
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if self.check(row, col, board):
                    # temp.append([row,col])
                    board[row][col] = 'Q'
                    solve(row+1)
                    # temp.pop()
                    board[row][col] = '.'
        solve(0)
        return res


    # check for valid placement
    def check(self, row: int, col: int, board: List[List[str]]) -> bool:
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row, col
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True