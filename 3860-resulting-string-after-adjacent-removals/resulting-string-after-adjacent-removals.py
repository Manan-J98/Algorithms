class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and self.isAdjacent(c, stack[-1]):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


    def isAdjacent(self, c1, c2):
        char1 = ord(c1) - ord('a')
        char2 = ord(c2) - ord('a')
        if ((char1 + 1) % 26 == char2) or ((char1 - 1) % 26 == char2):
            return True
        return False

        