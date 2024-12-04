class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        s2 = s[::-1]
        dp = [[0] * (m+1) for _ in range(m+1)]

        for row in range(m+1):
            dp[row][0] = 0
        
        maxLength = 0
        endIndex = 0
        for i in range(1, m+1):
            for j in range(1, m+1):
                if s[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1] # increase count but does not affect our answer because index mismatch, ie not a substring

                    if dp[i][j] > maxLength and (i-dp[i][j] == m - j): # checks that the index in the reversed string is matching
                        maxLength = dp[i][j]
                        endIndex = i
        startIndex = endIndex - maxLength
        return s[startIndex:endIndex]
        