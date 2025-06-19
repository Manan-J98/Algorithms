class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        minVal = nums[0]
        for num in nums:
            if num-minVal > k:
                res += 1
                minVal = num
        return res + 1
                