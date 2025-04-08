class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uni = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in uni:
                return math.ceil((i+1)/3)
            else:
                uni.add(nums[i])
        return 0