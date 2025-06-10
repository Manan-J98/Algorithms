class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        newS, newT = self.parse(s), self.parse(t)
        return newS == newT
    
    def parse(self, s) -> str:
        res = ""
        p = len(s)-1
        count = 0
        while p >= 0:
            if s[p] == "#":
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    res += s[p]
            p -= 1
        return res