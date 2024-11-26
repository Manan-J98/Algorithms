class Solution:
    def minCut(self, s: str) -> int:
        memo = {}
        n = len(s)

        # pre computing palindromes 
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True  # Single characters are palindromes
        for length in range(2, n + 1):  # Check substrings of all lengths
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = is_palindrome[i + 1][j - 1]
        def solve(i, j):
            # base condition
            if i >= j or is_palindrome[i][j]:
                return 0
            if (i, j) in memo:
                return memo[(i,j)]
            res = float('inf')
            for k in range(i, j):
                if is_palindrome[i][k]: # only if left partition is palindrome, check for right
                    temp = 1 + solve(k + 1, j)  # 1 cut + solve for the right partition
                    res = min(res, temp)
            memo[(i, j)] = res
            return res

        return solve(0, n-1)
        

            
    
    def isPalindrome(self, s, i, j) -> bool:
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True  