class Solution:

    # main intuition: use binary search twice 
    # once for lowerBound and once for upperBound

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.getStart(nums, target)
        right = self.getEnd(nums, target)
        return [left, right]

    def getStart(self, nums, target) -> int:
        l, r = 0, len(nums)-1
        result = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                result = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return result
            
    def getEnd(self, nums, target) -> int:
        l, r = 0, len(nums) - 1
        result = -1  # Initialize result to -1 to handle cases where target is not found
        while l <= r:  # Use <= to properly narrow the search range
            mid = (l + r) // 2
            if nums[mid] == target:
                result = mid  # Update result to the current mid index
                l = mid + 1  # Continue searching to the right to find the last occurrence
            elif nums[mid] < target:
                l = mid + 1  # Move right if the mid value is less than the target
            else:
                r = mid - 1  # Move left if the mid value is greater than the target
        return result
