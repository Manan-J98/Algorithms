from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        # If k is 0, return an array of zeros
        if k == 0:
            return [0] * n
        
        # Initialize result array
        result = [0] * n
        
        # Determine the sliding window range
        start, end = (1, k) if k > 0 else (k, -1)
        
        # Compute the initial window sum
        window_sum = sum(code[i % n] for i in range(start, end + 1))
        
        for i in range(n):
            # Assign the current sum to the result
            result[i] = window_sum
            
            # Update the sliding window
            window_sum -= code[(i + start) % n]
            window_sum += code[(i + end + 1) % n]
        
        return result
