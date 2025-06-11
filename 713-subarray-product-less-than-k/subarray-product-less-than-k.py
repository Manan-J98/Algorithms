class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0,0
        p = 1
        res = 0
        while right < len(nums):
            p = nums[right] * p
            while left < right and p >= k:
                p = p / nums[left]
                left += 1
            if p < k:
                res += right - left + 1
            right += 1
        return res