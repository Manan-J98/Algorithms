class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        freq = Counter(s)
        stack = []
        for char in s:
            freq[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)
