class Solution:
    # main intution: sort array
    # count pairs for both ranges, upper and lower
    # call binary search twice. once to get how many are under upper, another to get how many are under lower
    # subtract lower from upper to get valid count
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()        
        def binarySearch(target):
            left, right = 0, len(nums)-1
            count = 0
            while left <= right:
                if nums[left] + nums[right] <= target:
                    count += (right-left)
                    left += 1
                else:
                    right -= 1
            return count

        upperCount = binarySearch(upper)
        lowerCount = binarySearch(lower-1) # not equal to lower

        return upperCount - lowerCount