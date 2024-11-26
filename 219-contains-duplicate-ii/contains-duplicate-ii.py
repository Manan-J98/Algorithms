class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}
        for index, num in enumerate(nums):
            if num in indexMap:
                if abs(indexMap[num] - index) <= k:
                    return True
            indexMap[num] = index
        return False