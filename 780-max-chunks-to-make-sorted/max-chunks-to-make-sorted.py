class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # greedy approach, make chunk as soon as possible 
        # compare curMax with index, in sorted array all elements before i would be less than i 

        curMax = 0
        chunks = 0
        for i in range(len(arr)):
            curMax = max(curMax, arr[i])

            if curMax == i:
                chunks += 1
        return chunks