class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}
        def cost(index, color):
            if index == 0:
                return costs[index][color]
            
            if (index, color) in memo:
                return memo[(index, color)]
            totalCost = costs[index][color]
            minPrevCost = float('inf')

            for i in range(3):
                if i != color:
                    newMin = cost(index-1, i)
                    minPrevCost = min(minPrevCost, newMin)
            memo[(index, color)] = totalCost + minPrevCost
            return memo[(index, color)]
            
        res = float('inf')
        for i in range(3):
            temp = cost(len(costs)-1, i)
            res = min(res, temp)
        return res