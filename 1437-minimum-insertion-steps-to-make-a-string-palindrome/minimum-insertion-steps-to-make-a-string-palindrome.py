class Solution:
    # main intuition: palindrom question are usually child questions of Longest common subsequence
    # get the length of LCS and subtract it from the total length
    # all the characters that are not in the LCS need to be added to the string to make it a palindrome
    def minInsertions(self, s: str) -> int:
        m = len(s)
        str2 = s[::-1]
        n = len(str2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for row in range(m+1):
            dp[row][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return m - dp[m][n]
        