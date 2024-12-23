class Solution:

    def __init__(self, nums: List[int]):
        self.indexMap = {}
        for index, num in enumerate(nums):
            if num in self.indexMap:
                self.indexMap[num].append(index)
            else:
                self.indexMap[num] = deque()
                self.indexMap[num].append(index)
        print(self.indexMap)



    def pick(self, target: int) -> int:
        if target in self.indexMap:
            res = self.indexMap[target].popleft()
            self.indexMap[target].append(res)
            return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)