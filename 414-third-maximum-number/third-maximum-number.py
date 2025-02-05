class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        count = 3
        i = len(nums)-1
        while i >= 0:
            if nums[i] != nums[i-1]:
                count -= 1
                if count == 0:
                    return nums[i]
            i -= 1
        return nums[-1]