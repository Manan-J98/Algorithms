class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if stack and stack[-1] > num:
                continue
            else:
                stack.append(num)
        return len(stack)