class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy approach
        # what is the max reachable at any point ? 
        # its index + val
        # if index > curMax then cannot reach end
        # curMax = max(curMax, index + val)
        maxReach = 0
        for index in range(len(nums)):
            if index > maxReach:
                return False
            maxReach = max(maxReach, index + nums[index])
            if maxReach >= len(nums)-1:
                return True