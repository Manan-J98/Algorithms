class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        def solve(index):
            if index >= len(cost):
                return 0
            if not cache[index] == -1:
                return cache[index]
            else:
                cost1 = solve(index+1)
                cost2 = solve(index+2)
                cache[index] = cost[index] + min(cost1, cost2)
                return cache[index]
        return min(solve(0), solve(1))