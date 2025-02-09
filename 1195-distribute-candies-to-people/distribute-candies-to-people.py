class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        give = 0
        while candies > 0:
            res[give % num_people] += min(candies, give+1)
            give += 1
            candies -= give
        return res