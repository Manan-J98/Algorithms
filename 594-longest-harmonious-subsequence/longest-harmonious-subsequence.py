class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        arr = sorted(list(freq.keys()))
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) == 1:
                res = max(res, freq[arr[i]] + freq[arr[i+1]])
        return res