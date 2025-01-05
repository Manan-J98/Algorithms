class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        uni = set(s)
        res = 0
        for char in uni:
            l, r = s.find(char), s.rfind(char)
            if l != -1 and r != -1 and l < r:
                for mid in set(s[l+1:r]):
                    res += 1
        return res