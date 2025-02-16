class Solution:
    def repeatedCharacter(self, s: str) -> str:
        uni = set()
        for char in s:
            if char in uni:
                return char
            else:
                uni.add(char)
        return "a"