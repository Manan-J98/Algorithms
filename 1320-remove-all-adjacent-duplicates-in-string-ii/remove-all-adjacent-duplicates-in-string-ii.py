class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                char, count = stack.pop()
                count += 1
                stack.append((char, count))
            else:
                stack.append((char, 1))
            if stack[-1][1] == k:
                stack.pop()
        return ''.join([char*count for char, count in stack])