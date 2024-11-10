class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countArray = [0] * 3
        for num in nums:
                countArray[num] += 1
        fp, sp = 0, 0
        while sp < len(nums):
            if countArray[fp] == 0:
                fp += 1
            else:
                nums[sp] = fp
                sp += 1
                countArray[fp] -= 1