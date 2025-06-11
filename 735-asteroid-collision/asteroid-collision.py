class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            skip = False
            if ast < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(ast):
                        stack.pop()
                    elif stack[-1] == abs(ast):
                        stack.pop()
                        skip = True
                        break
                    else:
                        skip = True
                        break
            if not skip:
                stack.append(ast)
        return stack