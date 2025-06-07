class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        if obstacleGrid[0][0] == 1:
            return 0
        def path(i, j):
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]) or obstacleGrid[i][j] == 1:
                return 0
            if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            rightPath = path(i+1, j)
            downPath = path(i, j+1)
            memo[(i,j)] = rightPath + downPath
            return memo[(i,j)]
        
        return path(0,0)



