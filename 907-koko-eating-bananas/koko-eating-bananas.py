class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2
            sum = 0
            for pile in piles:
                sum += math.ceil(pile / k)
            if sum <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res