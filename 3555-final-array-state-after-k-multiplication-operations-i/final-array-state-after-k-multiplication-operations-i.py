class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(val, index) for index, val in enumerate(nums)]
        heapify(heap)
        for i in range(k):
            val, index = heappop(heap)
            val = val * multiplier
            heappush(heap, (val, index))
            nums[index] = val
        return nums