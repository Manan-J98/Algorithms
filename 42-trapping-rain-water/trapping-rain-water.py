class Solution:
    def trap(self, height: List[int]) -> int:
        # maxLeft, maxRight = [], [0] * len(height)
        # curMax = 0
        # res = 0
        # for h in height:
        #     maxLeft.append(curMax)
        #     curMax = max(curMax, h)
        # curMax = 0
        # for i in range(len(height)-1, -1, -1):
        #     maxRight[i] = curMax
        #     curMax = max(curMax, height[i])
        # for i in range(len(height)):
        #     trap = min(maxLeft[i], maxRight[i]) - height[i]
        #     if trap > 0:
        #         res += trap
        # return res

        # TWO POINTER APPROACH
        left, right = 0, len(height)-1
        leftMax = rightMax = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    res += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    res += rightMax - height[right]
                right -= 1
        return res


