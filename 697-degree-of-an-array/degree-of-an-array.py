class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
    # Dictionaries to track frequency, first, and last indices
        freq = defaultdict(int)
        first = {}
        last = {}
        
        for index, num in enumerate(nums):
            # Count frequency
            freq[num] += 1
            # Record the first occurrence
            if num not in first:
                first[num] = index
            # Always update the last occurrence
            last[num] = index
        
        # Determine the degree of the array
        degree = max(freq.values())
        
        # Find the shortest subarray with the same degree
        res = float('inf')
        for key, val in freq.items():
            if val == degree:
                res = min(res, last[key] - first[key] + 1)
        
        return res


