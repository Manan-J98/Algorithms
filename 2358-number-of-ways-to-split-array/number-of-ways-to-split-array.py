class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        curSum, totalSum = 0, sum(nums)
        res = 0
        for i in range(len(nums)-1):
            curSum += nums[i]
            if curSum >= (totalSum - curSum):
                res += 1
        return res