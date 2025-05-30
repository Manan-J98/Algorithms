class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for i in range(1, len(nums)+1):
            self.prefix.append(self.prefix[i-1] + nums[i-1])
        print(self.prefix)


    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefix[left]
        rightSum = self.prefix[right+1]
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)