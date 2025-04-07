class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        temp = self.arr[:]
        for i in range(len(temp)-1, -1, -1):
            index = random.randint(0, i)
            temp[index], temp[i] = temp[i], temp[index]
        print(temp)
        return temp


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()