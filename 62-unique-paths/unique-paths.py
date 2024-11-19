class Solution:
    # main intuition: build recursive solution and then memoize
    # we have two choices either move towards right or towards the bottom
    # base case is when we are at the destination
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def pathCount(i,j):

            if (i, j) in memo:
                return memo[(i,j)]

            if i == (m-1) and j == (n-1):
                return 1

            paths = 0
            
            if i < m: # can move right
                paths += pathCount(i+1, j)
            if j < n: # can move down
                paths += pathCount(i, j+1)
            
            memo[(i,j)] = paths
            return paths
        return pathCount(0,0)

        