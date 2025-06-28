class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [(-val, index) for index, val in enumerate(nums)]
        heapq.heapify(heap)
        res = [None] * len(nums)

        while k > 0:
            val, index = heapq.heappop(heap)
            res[index] = -val
            k -= 1
        return [val for val in res if val != None]

