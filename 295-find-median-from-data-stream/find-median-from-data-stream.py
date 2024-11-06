import heapq
class MedianFinder:
    # main intuition, partion the array into two parts, left is always smaller than right [1,2], [3,4]
    # we need max value from smaller partition, min value from larger partition
    # use heaps maxHeap for small, minHeap for large
    # get median
    def __init__(self):
        self.small = [] # maxHeap
        self.large = [] # minHeap
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # make sure length of two heaps is approximately same
        if len(self.small) > len(self.large) + 1:
            temp = -1 * heapq.heappop(self.small) # pop max value and push in large partition
            heapq.heappush(self.large, temp)
        elif len(self.large) > len(self.small) + 1: 
            temp = heapq.heappop(self.large) # pop min value and put in small partition
            heapq.heappush(self.small, -1 * temp)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()