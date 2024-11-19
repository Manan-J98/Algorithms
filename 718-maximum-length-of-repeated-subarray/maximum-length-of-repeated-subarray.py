class Solution:
    # dynamic programming
    # 2 options
    # first, if numbers match then, increase index for both and continue for rest subarray
    # second, if numbers do not match, either increase index for nums1 and same for nums2 or opposite
    # need to reset count as this is subset and not subsequence - how ? 
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for row in range(n+1):
            dp[row][0] = 0
        
        max_val = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_val = max(max_val, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_val

                 
            
