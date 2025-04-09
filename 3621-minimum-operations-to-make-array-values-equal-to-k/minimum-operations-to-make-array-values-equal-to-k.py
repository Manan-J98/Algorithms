class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        res = 0
        for key, val in freq.items():
            if key < k:
                return -1
            if key != k:
                res += 1
        return res