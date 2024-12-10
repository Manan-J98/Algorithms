class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def solve(index):
            # Base case: If we reach or exceed the last index, no more jumps are needed
            if index >= len(nums) - 1:
                return 0
            
            # If already computed, return the cached result
            if index in memo:
                return memo[index]

            # Initialize the minimum jumps to a large value
            min_jumps = float('inf')

            # Explore all possible jumps from the current position
            for jump in range(1, nums[index] + 1):
                min_jumps = min(min_jumps, 1 + solve(index + jump))
            
            # Cache the result
            memo[index] = min_jumps
            return min_jumps

        return solve(0)
