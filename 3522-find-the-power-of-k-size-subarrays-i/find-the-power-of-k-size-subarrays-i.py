from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Initialize pointers
        first, last = 0, k - 1
        res = []

        if k == 1:
            return nums
        
        # Pre-check if the first window is sorted
        is_sorted = True
        for i in range(first, last):
            if nums[i] >= nums[i + 1] or nums[i] + 1 != nums[i + 1]:
                is_sorted = False
                break
        
        # Process the first window
        res.append(max(nums[first:last + 1]) if is_sorted else -1)
        
        # Slide the window
        while last + 1 < len(nums):
            # Move the window
            first += 1
            last += 1
            
            # Update the sorted condition incrementally
            if is_sorted:
                # Check the two points that could invalidate the sorted condition
                if nums[last - 1] >= nums[last] or nums[last - 1] + 1 != nums[last]:
                    is_sorted = False
            else:
                # Recheck the full window if previously unsorted
                is_sorted = True
                for i in range(first, last):
                    if nums[i] >= nums[i + 1] or nums[i] + 1 != nums[i + 1]:
                        is_sorted = False
                        break
            
            # Append the result for the current window
            res.append(max(nums[first:last + 1]) if is_sorted else -1)
        
        return res
