class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        maxVal = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], 0, i))
            maxVal = max(nums[i][0], maxVal)
        res = [heap[0][0], maxVal]
        while True:
            val, idx, listIndex = heapq.heappop(heap)
            idx = idx + 1
            if idx < len(nums[listIndex]):
                heapq.heappush(heap, (nums[listIndex][idx], idx, listIndex))
                maxVal = max(maxVal, nums[listIndex][idx])
                minVal = heap[0][0]
                if maxVal - minVal < res[1] - res[0]:
                    res = [minVal, maxVal]
            else:
                break
        return res