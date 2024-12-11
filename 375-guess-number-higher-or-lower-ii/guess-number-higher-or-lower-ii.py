class Solution:
    # main intution: MCM pattern
    # finding i and j, 1 to n should be fine
    # finding the base case, i >= j: return 0, guessed correct
    # two sets, i to k, k+1 to j
    # temp ans 
    def getMoneyAmount(self, n: int) -> int:
        
        def solve(i, j):
            if i >= j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            minAmount = float('inf')
            for k in range(i, j+1):
                temp =  k + max(solve(i, k-1), solve(k+1, j))
                minAmount = min(minAmount, temp)
            memo[(i,j)] = minAmount
            return memo[(i,j)]
        memo = {}
        return solve(1, n)