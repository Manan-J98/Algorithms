class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        maxReach = 0
        currentEnd = 0
        
        for i in range(len(nums) - 1):  # We don't need to process the last index
            maxReach = max(maxReach, i + nums[i])  # Update the furthest reach
            
            if i == currentEnd:  # If we've reached the end of the current jump range
                jumps += 1       # Increment the jump count
                currentEnd = maxReach  # Update the current range to the furthest reach
                
                if currentEnd >= len(nums) - 1:  # If we can reach the end
                    return jumps
        
        return jumps  # Return jumps after the loop
