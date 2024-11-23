class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        if len(s) > len(t):
            return False
        for char in t:
            if p1 < len(s) and char == s[p1]:
                p1 += 1
        return p1 == len(s)