class Solution:
    # can check for palindrome from middle char and keep expanding 
    # only catch is that we have to write two functions for even and odd length palindromes
    # once you find palindrome, increment the result
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # for odd lengths
            left, right = i, i
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            
            # for even lengths
            left, right = i, i + 1
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            
        return res
        