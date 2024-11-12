class Solution:
    # main intuition: 0/1 Knapsack i.e if to include the element or not.
    # need to subsets s1 and s2 where s1 has all positive elements and s2 has negative, take - common -> problem becomes similar to
    # finding subsets with diff = target
    # s1 + s2 = sum(nums)
    # s1 - s2 = target
    # s1 = sum + target / 2
    # find s1 
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = abs(target)
        arrSum = sum(nums)

        if arrSum < target:
            return 0
        if not ((arrSum + target) % 2 == 0):
            return 0
        n = len(nums)
        s1 = (target + arrSum) // 2  
        dp = [[0] * (s1+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(s1+1):
                if nums[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-nums[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][s1]

