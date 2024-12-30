class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def solve(index, holding):
            if index == len(prices):
                return 0
            if (index, holding) in memo:
                return memo[(index, holding)]
            if holding:
                # choice 1 - buy
                sell = prices[index] + solve(index+1, 0)
                skip = solve(index+1, 1)
                memo[(index,holding)] = max(sell, skip)

            else:
                buy = -prices[index] + solve(index+1, 1)
                skip = solve(index+1, 0)
                memo[(index,holding)] = max(buy, skip)
            return memo[(index, holding)]
        return solve(0,0)
            
            
