class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        heap = []
        res = []
        for r in restaurants:
            ID, rating, isVegan, price, distance = r[0], r[1], r[2], r[3], r[4]
            if veganFriendly == 1:
                if isVegan and price <= maxPrice and distance <= maxDistance:
                    heapq.heappush(heap, (-rating, -ID))
            else:
                if price <= maxPrice and distance <= maxDistance:
                    heapq.heappush(heap, (-rating, -ID))

        while heap:
            res.append(-heapq.heappop(heap)[1])
        return res
        
        



