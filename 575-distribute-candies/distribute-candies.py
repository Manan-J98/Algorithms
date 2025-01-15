class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies = Counter(candyType)
        limit = len(candyType) // 2
        maxCandies = len(candies.keys())
        return maxCandies if maxCandies < limit else limit