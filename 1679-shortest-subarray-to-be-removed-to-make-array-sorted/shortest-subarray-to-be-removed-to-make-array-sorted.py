class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # get longest prefix 

        left = 0
        while left + 1 < n and arr[left] <= arr[left+1]:
            left += 1
        # if longest prefix is the whole array, then array is already sorted
        if left == n-1:
            return 0

        # longest decreasing suffix
        right = n-1
        while right > 0 and arr[right-1] <= arr[right]:
            right -= 1
        
        # find the subarray to remove
        res = min(n-left-1, right)
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j-i-1)
                i += 1
            else:
                j += 1
        return res