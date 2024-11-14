class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1)-1, len(text2)-1
        memo = {}
        def lcs(text1, text2, n, m):
            # base case 
            if n == -1 or m == -1:
                return 0 # if anyone of the string is null, no match possible

            if (n,m) in memo:
                return memo[(n,m)]
            else:
                # case 1, when chars match
                if text1[n] == text2[m]:
                    memo[(n,m)] = 1 + lcs(text1, text2, n-1, m-1)
                    return memo[(n,m)]
                # case 2, when they don't match
                # 2 options, either move text1 or text2, return whatever gives max
                else:
                    memo[(n,m)] = max(lcs(text1, text2, n-1, m), lcs(text1, text2, n, m-1))
                    return memo[(n,m)]
        return lcs(text1, text2, n, m)
