class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort() # sort on the basis of price 
        res = []

        max_beauty = 0
        for index in range(len(items)): # store max beauty till now for that price
            max_beauty = max(max_beauty, items[index][1])
            items[index][1] = max_beauty 

        for price in queries: # outer loop to go through all queries
            l, r = 0, len(items)-1
            match = 0
            while l <= r:
                mid = (l + r) // 2

                if items[mid][0] <= price:
                    match = items[mid][1] # set max_beauty till now and search for higher price
                    l = mid + 1
                else: # continue to go left cause not in range of query
                    r = mid - 1
            res.append(match)
        return res

