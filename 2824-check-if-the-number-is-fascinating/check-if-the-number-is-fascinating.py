class Solution:
    def isFascinating(self, n: int) -> bool:
        mod = str(n) + str(2*n) + str(3*n)
        return sorted(mod) == [str(i+1) for i in range(9)]