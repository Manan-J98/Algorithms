class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(str1) and p2 < len(str2):
            if ((ord(str1[p1]) + 1) - ord(str2[p2])) % 26 == 0 or str1[p1] == str2[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        return p2 == len(str2)
        