class Solution:
    def makeFancyString(self, s: str) -> str:
        ptr = 0
        result = ""
        while ptr + 2 < len(s):
            if s[ptr] == s[ptr+1] and s[ptr] == s[ptr+2]:
                print("same")
            else:
                result += s[ptr]
            ptr = ptr+1
        result += s[ptr:]
        return result