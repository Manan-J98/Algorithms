class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = nums[:]
        heapify(heap)
        
        operations = 0

        while len(heap) > 1 and heap[0] < k:  # Run while heap[0] < k
            x = heappop(heap)
            y = heappop(heap)
            heappush(heap, x * 2 + y)
            operations += 1

        return operations if heap[0] >= k else -1  # If last element is still < k, return -1
