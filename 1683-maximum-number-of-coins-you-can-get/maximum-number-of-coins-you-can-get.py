class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i,j = 0, len(piles)-1
        res = 0
        while (j - i) >= 2 :
            res += piles[j-1]
            j = j - 2
            i = i + 1
        return res