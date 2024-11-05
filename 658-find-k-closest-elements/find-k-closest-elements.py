class Solution:
    # main intuition - using a heap
    # create a max heap and pop when size of heap > k
    # store value and difference as tuple, sort on the basis of diff from x
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapify(heap)
        for val in arr:
            heappush(heap, (-(abs(val-x)), -val))
            if len(heap) > k:
                temp = heappop(heap)
        res = sorted([-t[1] for t in heap])
        return res
