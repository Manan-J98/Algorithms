class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapify(heap)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(heap, -1 * matrix[j][i])
                if len(heap) > k:
                    heappop(heap)
        return -heap[0]
