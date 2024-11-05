class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l <= r:
            mid = (l + r) // 2
            left = nums[mid-1] if mid-1 >= 0 else float('-inf')
            right = nums[mid+1] if mid+1 < len(nums) else float('-inf')

            if nums[mid] > left and nums[mid] > right:
                return mid
            elif nums[mid] > left:
                l = mid + 1
            else:
                r = mid - 1