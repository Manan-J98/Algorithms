class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for char in s:
            freq[char] = (freq[char] + 1) if char in freq else 1
        for char in t:
            if char not in freq:
                return char
            else:
                freq[char] -= 1
                if freq[char] == -1:
                    return char
            