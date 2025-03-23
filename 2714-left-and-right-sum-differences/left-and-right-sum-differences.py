class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        cur = total
        res = [0] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            cur = cur-nums[i]
            res[i] = cur
        cur = total
        for i in range(len(nums)):
            cur = cur-nums[i]
            res[i] = abs(res[i]-cur)
        return res