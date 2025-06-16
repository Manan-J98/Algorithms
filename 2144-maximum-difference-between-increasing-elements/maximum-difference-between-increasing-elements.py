class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minVal = float('inf')
        res = -1
        for num in nums:
            minVal = min(num, minVal)
            res = max(res, num-minVal)
        return res if res > 0 else -1