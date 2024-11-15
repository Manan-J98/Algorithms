class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # base case 
        def getCombinations(nums, curSum, out):
            if curSum > target or not nums:
                return 
            if curSum == target:
                res.append(out.copy())
                return 
            out.append(nums[0]) # choice 1,  use the cur number and call again on the whole array
            getCombinations(nums, curSum + nums[0], out)
            out.pop() # remove cur choice and call again starting from next element
            getCombinations(nums[1:], curSum, out) # choice2, dont use cur element
        getCombinations(nums, 0, [])
        return res