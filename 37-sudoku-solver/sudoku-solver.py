class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize constraints
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def solve(row, col):
            # base case 
            if row == 8 and col == 9:
                return True
            if col == 9:
                return solve(row+1, 0)
            
            # if cell not empty, skip
            if board[row][col] != ".":
                return solve(row, col+1)
            for val in map(str, range(1, 10)):
                box_idx = (row // 3) * 3 + (col // 3)
                if val not in rows[row] and val not in cols[col] and val not in boxes[box_idx]:
                    board[row][col] = val
                    rows[row].add(val)
                    cols[col].add(val)
                    boxes[box_idx].add(val)

                    if solve(row, col + 1):
                        return True

                    # Backtrack
                    board[row][col] = "."
                    rows[row].remove(val)
                    cols[col].remove(val)
                    boxes[box_idx].remove(val)
            return False
        solve(0,0)
        
    # def canPlace(self, row, col, grid, val) -> bool:
    #     # row check and col check
    #     for i in range(9):
    #         if grid[i][col] == val or grid[row][i] == val:
    #             return False
    #     # subgrid check
    #     for i in range(3):
    #         for j in range(3):
    #             s_row, s_col = ((row//3) * 3) + i, ((col//3) * 3) + j
    #             if grid[s_row][s_col] == val:
    #                 return False
    #     return True

                