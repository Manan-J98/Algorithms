class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        cost = 0
        if n <=k and m <=k:
            return cost
        if n > k:
            cost += (n-k) * k
        if m > k:
            cost += (m-k) * k
        return cost
        