class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def robbing(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]

            option1 = robbing(index+1)
            option2 = nums[index] + robbing(index+2)

            memo[index] = max(option1, option2)
            return memo[index]
        return robbing(0)
        