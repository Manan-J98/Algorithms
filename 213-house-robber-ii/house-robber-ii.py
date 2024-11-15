class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:  # Handle the single house case
            return nums[0]

        def solve(arr):
            cache = [-1] * len(arr)  # Separate cache for each subproblem

            def helper(index):
                if index >= len(arr):
                    return 0
                if cache[index] != -1:
                    return cache[index]
                # Rob this house or skip it
                choice1 = arr[index] + helper(index + 2)
                choice2 = helper(index + 1)
                cache[index] = max(choice1, choice2)
                return cache[index]

            return helper(0)

    # Solve both subproblems: excluding the first or the last house
        return max(solve(nums[1:]), solve(nums[:-1]))
