class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curSum = 0
        subArr = 0
        prefixSum = {curSum: 1}

        for i in range(len(nums)):
            curSum += nums[i] % 2
            if curSum - k in prefixSum:
                subArr += prefixSum[curSum-k]
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return subArr