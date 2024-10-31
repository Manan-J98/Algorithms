class Solution:
    # base case - when only one guy remains
    # hypothesis - a func solve(arr, k) that returns the last guy
    # smaller case - remove first guy, solve for rest
    # induction - no induction step as the person removed is no longer needed
    def findTheWinner(self, n: int, k: int) -> int:
        k = k-1
        players = [i for i in range(n)]

        def find(players, k, index) -> int:
            # base case
            if len(players) == 1:
                return players[0] # last person standing
            index = (index + k) % len(players) # validate index for circular loop
            players.pop(index) # remove loser
            find(players, k, index) # keep playing 
        find(players, k, 0)
        return players[0]+1


            
        