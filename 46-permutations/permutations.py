class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(start):
            # base case 
            if start == len(nums)-1:
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                solve(start+1)
                # backtrack to original array
                nums[i], nums[start] = nums[start], nums[i]
        solve(0)
        return res
            