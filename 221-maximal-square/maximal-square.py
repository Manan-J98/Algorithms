class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = {}
        def solve(i, j):
            if i < 0 or j < 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if matrix[i][j] == "1":
                memo[(i,j)]  = min(solve(i-1, j),
                        solve(i, j-1),
                        solve(i-1, j-1)
                        ) + 1
            else:
                memo[(i,j)] = 0
            return memo[(i,j)]  

        res = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, solve(i, j))
        return res * res
