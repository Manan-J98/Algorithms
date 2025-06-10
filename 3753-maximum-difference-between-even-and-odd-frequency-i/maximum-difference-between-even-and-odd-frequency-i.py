class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd, minEven = float('-inf'), float('inf')
        freq = Counter(s)

        for key, value in freq.items():
            if value % 2 == 0:
                minEven = min(value, minEven)
            else:
                maxOdd = max(value, maxOdd)
        return maxOdd - minEven