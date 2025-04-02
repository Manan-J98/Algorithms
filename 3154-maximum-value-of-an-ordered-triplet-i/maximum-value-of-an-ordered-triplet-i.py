class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxElement, maxDiff, maxTriplet = float("-inf"), 0, 0
        for i in range(len(nums)):
            maxTriplet = max(maxTriplet, maxDiff * nums[i])
            maxElement = max(maxElement, nums[i])
            maxDiff = max(maxDiff, maxElement - nums[i])
        return maxTriplet