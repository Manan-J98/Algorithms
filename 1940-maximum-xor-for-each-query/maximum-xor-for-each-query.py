class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        xor = None
        for i in range(len(nums)):
            if not xor:
                xor = nums[i]
            else:
                xor = xor ^ nums[i]
            res.append(xor ^ (int(math.pow(2, maximumBit))-1))
        res.reverse()
        return res
