class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # use the flipping logic 
        # each number is point to an index and we need all repeated elements 
        # if a number is already flipped, add to res

        res = []
        for i in range(len(nums)):
            flipIndex = abs(nums[i])-1
            if nums[flipIndex] < 0:
                res.append(abs(nums[i]))
            else:
                nums[flipIndex] = -nums[flipIndex]
        return res