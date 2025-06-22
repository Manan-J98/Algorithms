class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        arr = list(freq.values())
        arr.sort()
        total = sum(arr)
        res = float('inf')
        for i in arr:
            maxAllowed = i + k
            keep = 0
            for j in arr:
                if i <= j <= maxAllowed:
                    keep += j
                elif j > maxAllowed:
                    keep += maxAllowed
            res = min(res, total-keep)
        return res
