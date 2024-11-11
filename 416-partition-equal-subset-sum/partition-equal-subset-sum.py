class Solution:
    # main intuition: if sum of all elements is odd, not possible to find a subset
    # if array has one subset where sum equals totalSum / 2 then the other subset already has the rest totalSum / 2
    # problem now becomes similar to subset sum problem
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0
        for num in nums:
            totalSum += num
        if not totalSum % 2 == 0:
            return False
        n = len(nums)
        totalSum = int(totalSum / 2)

        dp  = [[False] * (totalSum+1) for _ in range(n+1)]
        for row in range(len(dp)):
            dp[row][0] = True
        
        # subset sum
        for i in range(1, n+1):
            for j in range(1, totalSum+1):
                if nums[i-1] <= j: # takefirst item and check if it can be included
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][totalSum]


        