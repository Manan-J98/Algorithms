class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indexMap = {}
        minCards = float('inf')
        for i in range(len(cards)):
            if cards[i] in indexMap:
                lastIndex = indexMap[cards[i]]
                minCards = min(minCards, i - lastIndex + 1)
            indexMap[cards[i]] = i

        return -1 if minCards == float('inf') else minCards