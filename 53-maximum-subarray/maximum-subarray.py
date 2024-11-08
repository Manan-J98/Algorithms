class Solution:
    # Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float('-inf')
        for index, val in enumerate(nums):
            curSum += val
            if curSum > maxSum:
                maxSum = curSum
                end = index # end index will only change if sum of seq > maxSum
            if curSum < 0: # only move start index if current sum is below 0
                start = index+1
                curSum = 0 # reset curSum
        return maxSum