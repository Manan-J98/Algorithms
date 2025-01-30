class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set() # tuple of rows, col to manage visited cells
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def solve(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            for d in directions:
                newRow, newCol = row + d[0], col + d[1]
                if solve(newRow, newCol, index+1):
                    return True
            visited.remove((row, col))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and solve(i, j, 0):
                    return True
        return False