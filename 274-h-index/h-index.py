class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hindex = 0
        for i, c in enumerate(citations):
            if i + 1 <= c:
                hindex = i + 1
            else:
                break
        return hindex
