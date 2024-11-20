class Solution:
    # main intuition: this is a child question of longest common subsequence
    # if i take the lcs and subtract it from str1+str2 I get the string that is the shortest common subsequence
    # i also need to print the sequence so i need to track the path from the dp table but upwards
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        res = []
        dp = [[0] * (n+1) for _ in range(m+1)]

        for row in range(m+1):
            dp[row][0] = 0
        
        # fill the dp table
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # traverse the path from bottom up
        i,j = m,n
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                res.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]: # this is how the table is filled max(dp[i-1][j], dp[i][j-1])
                res.append(str1[i-1])
                i -= 1
            else:
                res.append(str2[j-1])
                j -= 1
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return ''.join(reversed(res))
 

        

