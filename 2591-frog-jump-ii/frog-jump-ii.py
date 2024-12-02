class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)

        if n == 2:
            return stones[1] - stones[0] # only one possible jump

        res = float('-inf')

        for i in range(2,n):
            res = max(res, stones[i] - stones[i-2])
        
        return res