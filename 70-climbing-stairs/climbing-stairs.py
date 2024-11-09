class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)

        def solve(curStep):
            # Base cases
            if curStep == n:
                return 1  # Reached the top
            if curStep > n:
                return 0  # Exceeded the top

            # Use cache if result is already computed
            if cache[curStep] != -1:
                return cache[curStep]

            # Recursive calls: move 1 step or 2 steps
            cache[curStep] = solve(curStep + 1) + solve(curStep + 2)
            return cache[curStep]

        # Start from step 0
        return solve(0)