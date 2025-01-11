class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = Counter(s)
        oddCount = sum(1 for val in freq.values() if val % 2 != 0)
        return False if (len(s) < k or oddCount > k) else True