class Solution:
    # main intuition: mcm pattern.
    # need to drop eggs starting from the bottom floor and get the threshold at which they break
    # return the minimum number of moves that we need to determin with certainity what the threshold is
    # two options, either the egg breaks in which case we go lower or it doesn't break in which case we go upper floor
    # to find the range of k, we can move from floor 1 for floor n
    def twoEggDrop(self, n: int) -> int:
        memo = {}
        def solve(eggs, floors):
            # if no floors then 0 tries, if 1 floor or 1 eggs then 1 try atleast
            if floors == 0 or floors == 1 or eggs == 1:
                return floors
            
            if (eggs, floors) in memo:
                return memo[(eggs, floors)]
            
            minTries = float('inf')
            for k in range(1, floors+1):
                # if egg breaks, move lower
                option1 = solve(eggs-1, k-1) # check only lower floors
                # if egg does not break, move up
                option2 = solve(eggs, floors-k)

                temp = 1 + max(option1, option2) # max cause we need worst case to determine with certainity
                minTries = min(minTries, temp)
            memo[(eggs, floors)] = minTries
            return memo[(eggs, floors)]
        return solve(2, n)
        


            
        