class Solution:
    # main intuition: game theory
    # we have two options as player1, either take the left val or take the right val = two recursive calls
    # now we need get max diff possible when player 2 plays optimally 
    # ex 1, 5, 2 - if choose 1, then player 2 takes 5 so diff -4 i.e player one cannot win if he takes left
    # same if he chooses 2, still cannot win as diff = -3 
    # we need max diff to check if he can win at all
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def maxDiff(left, right):
            if left == right:
                return nums[left]
            
            if (left, right) in memo:
                return memo[(left,right)]
            else:
                # diff from right of subarray if we take left
                choice1 = nums[left] - maxDiff(left+1, right)
                # diff from left of subarray if we take right
                choice2 = nums[right] - maxDiff(left, right-1)

            # get max diff to see if win is possible or no
                memo[(left,right)] = max(choice1, choice2)
                return memo[(left,right)]
        
        left, right = 0, len(nums)-1
        return maxDiff(left,right) >= 0
            
