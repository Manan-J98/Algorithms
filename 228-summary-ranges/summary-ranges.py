class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0 
        res = []
        while i < len(nums):
            end = i
            while end < len(nums)-1 and nums[end] + 1 == nums[end+1]:
                end += 1
            if i == end:
                res.append(str(nums[i]))
            else:
                res.append(f"{nums[i]}->{nums[end]}")
            i = end + 1
        return res