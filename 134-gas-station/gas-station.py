class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)
        if totalGas < totalCost:
            return -1
        curGas = 0
        res = -1
        for (index, g) in enumerate(gas):
            curGas += g - cost[index]
            if curGas < 0:
                curGas = 0
                res = -1
            else:
                if res == -1:
                    res = index
        return res