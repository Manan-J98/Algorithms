class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def solve(index, out):
            if index  == len(nums):
                res.append(out[:])
                return
            
            # choice 1 - take
            out.append(nums[index])
            solve(index+1, out)
            out.pop()

            # choice 2 - skip
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1     
            solve(index + 1, out)
        solve(0, [])
        return res