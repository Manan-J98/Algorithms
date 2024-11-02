import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        heapq.heapify(heap)
        for index, point in enumerate(points):
            x = point[0]
            y = point[1]
            ed = math.sqrt(pow(x,2) + pow(y,2))
            heapq.heappush(heap, (ed, index)) # create a min heap, store euclidean distance and index
        for i in range(k):
            index = heapq.heappop(heap)[1] # retrieve index for lower euclidean distance k times
            res.append(points[index]) # append to result array
        return res
