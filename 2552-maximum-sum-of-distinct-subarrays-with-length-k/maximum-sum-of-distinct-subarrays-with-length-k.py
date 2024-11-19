class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = 0
        curSum = 0
        seen = set()
        left = 0

        for right in range(len(nums)):

            while nums[right] in seen: # if we keep finding repetitive elements, keep moving window
                seen.remove(nums[left])
                curSum -= nums[left]
                left += 1
            
            seen.add(nums[right])
            curSum += nums[right]

            if right-left+1 == k: # found the window size with all unique elements
                maxSum = max(curSum, maxSum)

                # move window
                seen.remove(nums[left])
                curSum -= nums[left]
                left += 1
        return maxSum


        
        


        


