class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftPrefix = [0] * len(nums)
        rightPrefix = [0] * len(nums)
        curSum = 0
        for i in range(len(nums)):
            leftPrefix[i] = curSum
            curSum += nums[i]
        print(leftPrefix)
        curSum = 0
        for i in range(len(nums)-1,-1,-1):
            rightPrefix[i] = curSum
            curSum += nums[i]
        print(rightPrefix)
        for i in range(len(nums)):
            if leftPrefix[i] == rightPrefix[i]:
                return i
        return -1
