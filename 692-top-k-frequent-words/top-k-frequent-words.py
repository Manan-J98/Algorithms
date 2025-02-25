class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        heapify(heap)
        for key, val in freq.items():
            heappush(heap, (-val, key))
        result = [heappop(heap)[1] for _ in range(k)]
        return result