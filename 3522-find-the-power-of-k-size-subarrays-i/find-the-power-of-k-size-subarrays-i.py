class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        first, last = 0, k-1
        res = []
        while last < len(nums):
            if self.checkSorted(nums[first:last+1]):
                res.append(max(nums[first:last+1]))
            else:
                res.append(-1)
            first += 1
            last += 1
        return res

    def checkSorted(self, arr):
        for i in range(len(arr)-1):
            if  arr[i] >= arr[i+1] or (arr[i] + 1 != arr[i+1]):
                return False
        return True
