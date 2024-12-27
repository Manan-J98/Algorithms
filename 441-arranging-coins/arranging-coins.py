class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        rows = 1
        while (n - rows) >= 0:
            n = n - rows
            rows += 1
        return rows-1
            