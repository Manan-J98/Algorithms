class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [], [0] * len(height)
        curMax = 0
        res = 0
        for h in height:
            maxLeft.append(curMax)
            curMax = max(curMax, h)
        curMax = 0
        for i in range(len(height)-1, -1, -1):
            maxRight[i] = curMax
            curMax = max(curMax, height[i])
        for i in range(len(height)):
            trap = min(maxLeft[i], maxRight[i]) - height[i]
            if trap > 0:
                res += trap
        return res

