class Solution:
    # start from 0,0 
    # two choices, either move right or down
    # we need the min of the two choices 
    # only way to reach i,j is from either top or left 
    # so we need min of these two and add the current val
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)-1
        n = len(grid[0])-1
        memo = {}
        def solve(i, j):
            if i == m and j == n:
                return grid[i][j]
            
            if (i, j) in memo:
                return memo[(i,j)]

            min_sum = float('inf')
            if i < m:
                # move down
                min_sum = min(min_sum, solve(i+1, j))
            if j < n:
                # move right
                min_sum = min(min_sum, solve(i, j+1))
                # now min_sum contains sum path from either left or top (whichever min)
            memo[(i,j)] = min_sum + grid[i][j]
            return memo[(i,j)]
        return solve(0, 0)
