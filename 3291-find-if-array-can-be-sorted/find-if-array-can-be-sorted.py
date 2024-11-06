class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevMax = float('-inf')
        curMax = float('-inf')
        curMin = float('inf')

        for i in range(len(nums)):
            curMax  = max(curMax, nums[i])
            curMin = min(curMin, nums[i])
            if not i >= len(nums)-1  and self.setBits(nums[i]) == self.setBits(nums[i+1]):
                continue
            else:
                if not prevMax == float('-inf') and prevMax > curMin:
                    return False
                prevMax = curMax
                curMax = float('-inf')
                curMin = float('inf')
        return True
    
    def setBits(self, n) -> int:
        ans = bin( n ) 
        return ans.count('1')

