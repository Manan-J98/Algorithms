class Solution:
    def possibleStringCount(self, word: str) -> int:
        stack = []
        res = 1
        for char in word:
            if stack and stack[-1] == char:
                res += 1
            stack.append(char)
        return res