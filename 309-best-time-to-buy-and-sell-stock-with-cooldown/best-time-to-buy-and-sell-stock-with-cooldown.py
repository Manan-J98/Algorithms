class Solution:
    # main intuition: what are the choices here
    # either sell, buy or cooldown
    # have to cooldown after selling 
    # need the max of these options
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def profit(index, isBuying):
            # base case
            if index >= len(prices):
                return 0 

            if (index, isBuying) in memo:
                return memo[(index, isBuying)] 

            # option 1
            if isBuying:
                buy = profit(index+1, not isBuying) - prices[index]
                cooldown = profit(index+1,isBuying) # status doesn't change for cooldown
                memo[(index, isBuying)] = max(buy, cooldown)
            else:
                sell = profit(index+2, not isBuying) + prices[index]
                cooldown = profit(index+1,isBuying)
                memo[(index, isBuying)] = max(sell, cooldown)
            return memo[(index, isBuying)]
        return profit(0, True)