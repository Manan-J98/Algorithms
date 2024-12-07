class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # check the number of operations needed for a specific ballsize
        def possible(ballsize):
            ops = 0
            for num in nums:
                if num > ballsize:
                    ops += ceil(num / ballsize) - 1 # 1 op divides into 2 parts so -1
                if ops > maxOperations:
                    return False
            return True
        
        left, right = 1, max(nums) # max ballsize right range
        while left < right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid # need to minimize
            else:
                left = mid + 1
        return left
