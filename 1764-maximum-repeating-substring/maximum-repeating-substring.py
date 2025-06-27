class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0
        temp = word
        while temp in sequence:
            temp += word
            res += 1
        return res