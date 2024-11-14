class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[float('inf')] * (amount+1) for _ in range(n+1)]

        for row in range(n+1):
            dp[row][0] = 0

        for col in range(1, amount+1):  # need to initialize second row as some cases will not be possible.
            if coins[0] % col == 0:
                dp[1][col] = coins[0] // col
            else :
                dp[1][col] = float('inf')
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]]) # add 1 way if choosing the coin else don't
                else:
                    dp[i][j] = dp[i-1][j]
        
        return -1 if dp[n][amount] == float('inf') else dp[n][amount]
