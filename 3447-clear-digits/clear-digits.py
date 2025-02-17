class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        res = ""
        for char in list(s):
            if char.isnumeric() and stack:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)