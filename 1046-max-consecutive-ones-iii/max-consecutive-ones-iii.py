class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        swaps = k
        max_window = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                swaps -= 1
            
            while swaps < 0:
                if nums[i] == 0:
                    swaps += 1
                i += 1
            max_window = max(max_window, j-i+1)
        return max_window
                    