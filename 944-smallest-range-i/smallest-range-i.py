class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = (nums[-1] - k) - (nums[0] + k)
        return 0 if res <= 0 else res