class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        memo = {}
        def solve(cur, prev):
            if cur == n:
                return []
            if (cur, prev) in memo:
                return memo[cur, prev]
            
            # choice 1 skip the element
            skip = solve(cur+1, prev)

            # choice 2 take the element if divisible
            take = []
            if prev == -1 or (nums[cur] % nums[prev]) == 0:
                take = [nums[cur]] + solve(cur+1, cur)
            
            memo[(cur,prev)] = take if len(take) > len(skip) else skip
            return memo[(cur, prev)]
        
        return solve(0, -1)