class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        move = 0
        stack = []
        for c in colors:
            if not stack or stack[-1] == c:
                stack.append(c)
            elif stack[-1] != c:
                stack = []
                stack.append(c)
            
            if len(stack) >= 3 and stack[-1] == "A":
                move += 1
            elif len(stack) >= 3 and stack[-1] == "B":
                move -= 1
        return move > 0

