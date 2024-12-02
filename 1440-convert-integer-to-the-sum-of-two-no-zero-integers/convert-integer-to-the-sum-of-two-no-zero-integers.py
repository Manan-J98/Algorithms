class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if not '0' in str(i) and not '0' in str(n-i):
                return [i, n-i]
