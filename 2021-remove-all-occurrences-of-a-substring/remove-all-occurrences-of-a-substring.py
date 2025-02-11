class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            if ''.join(stack[-len(part):]) == part:
                del stack[-len(part):]

        return ''.join(stack)