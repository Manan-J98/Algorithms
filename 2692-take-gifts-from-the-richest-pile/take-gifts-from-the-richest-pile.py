class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [(-1 * gift) for gift in gifts]
        heapify(heap)
        while k > 0:
            max_gift = -1 * heappop(heap)
            print(max_gift)
            max_gift = floor(math.sqrt(max_gift))
            heappush(heap, -1*max_gift)
            k -= 1
        return sum([-1*val for val in heap])