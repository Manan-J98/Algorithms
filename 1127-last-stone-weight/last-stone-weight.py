import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for stone in stones:
            heapq.heappush(heap,-1 * stone) # create max heap to keep track of heaviest stone
        while len(heap) > 1:
            x = -heapq.heappop(heap) # get heaviest stone
            y = -heapq.heappop(heap) # get second heaviest stone
            if not (x == y): # if not same weight, push result to heap
                heapq.heappush(heap, -1 * (x-y))
        return -heap[0] if len(heap) > 0 else 0