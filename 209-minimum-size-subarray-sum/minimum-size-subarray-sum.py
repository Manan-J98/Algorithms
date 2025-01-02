class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curSum = 0,0
        windowSize = float('inf')
        for r in range(len(nums)):
            curSum = curSum + nums[r]
            while curSum >= target:
                windowSize = min(r-l+1, windowSize)
                curSum -= nums[l]
                l += 1
        return windowSize if windowSize != float('inf') else 0
