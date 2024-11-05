class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapify(heap)
        res = []
        freq = defaultdict(int)
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key, value in freq.items():
            heappush(heap, (value, key))
            if len(heap) > k:
                heappop(heap)
        res = [t[1] for t in heap]
        return res
