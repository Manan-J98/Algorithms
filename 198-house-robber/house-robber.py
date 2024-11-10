class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def solve(index):
            if index >= len(nums):
                return 0
            if not cache[index] == -1:
                return cache[index]
            choice1 = nums[index] + solve(index+2)
            choice2 = solve(index+1)
            cache[index] = max(choice1,choice2)
            return cache[index]
        return solve(0)