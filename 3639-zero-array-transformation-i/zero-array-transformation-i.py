class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums)+1)
        for q in queries:
            diff[q[0]] += 1
            diff[q[1]+1] -= 1
        prefix = []
        curSum = 0
        for val in diff:
            prefix.append(curSum)
            curSum += val
        for i in range(len(nums)):
            if not (nums[i] <= prefix[i+1]):
                return False

        return True