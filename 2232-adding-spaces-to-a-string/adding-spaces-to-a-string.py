class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        sp = 0
        for index in range(len(s)):
            if sp < len(spaces) and index == spaces[sp]:
                res += " " + s[index]
                sp += 1
            else:
                res += s[index]
        return res
