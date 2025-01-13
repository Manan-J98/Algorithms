class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        res = len(s)
        for key, val in freq.items():
            i = val
            while i > 2:
                res -= 2
                i -= 2
        return res