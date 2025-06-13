class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        totalSum = sum(nums)

        currMax = 0
        maxSum = nums[0]

        currMin = 0
        minSum = nums[0]

        for num in nums:
            currMax = max(num, currMax + num)
            maxSum = max(maxSum, currMax)

            currMin = min(num, currMin + num)
            minSum = min(minSum, currMin)

        if maxSum < 0:
            return maxSum
        
        return max(maxSum, totalSum-minSum)
