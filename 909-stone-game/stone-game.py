class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # main intution: function should return the total score difference
        # no need to track turns or score
        # 2 choices - take left and subtract opponents optimal choice
        # take right and subtract " "
        memo = {}
        def solve(i, j):
            if i > j:
                return 0 # no choice left
            if (i, j) in memo:
                return memo[(i,j)]
            take_left = piles[i] - solve(i+1, j)
            take_right = piles[j] - solve(i, j-1) # recursive call represents opp optimal choice

            memo[(i,j)] = max(take_left, take_right)

            return memo[(i,j)] # need max choice for optimal pick
        return solve(0, len(piles)-1) > 0 # if diff +ve, Alice wins 