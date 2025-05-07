class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, res  = [], []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            # Start collecting results once the first window is complete
            if i >= k - 1:
                # Remove elements that are out of the window
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])  # max value in window

        return res
            
