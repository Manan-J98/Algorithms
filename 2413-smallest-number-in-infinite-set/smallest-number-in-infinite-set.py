class SmallestInfiniteSet:

    def __init__(self):
        self.removedBefore = set()
        self.inf = [i for i in range(1, 1001)]
        heapify(self.inf)

    def popSmallest(self) -> int:
        remove = heappop(self.inf)
        self.removedBefore.add(remove)
        return remove

    def addBack(self, num: int) -> None:
        if num in self.removedBefore:
            heappush(self.inf, num)
            self.removedBefore.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)