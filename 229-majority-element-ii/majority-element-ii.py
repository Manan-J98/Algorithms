class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []
        for num in nums:
            if freq[num] > len(nums) / 3:
                freq[num] = -1
                res.append(num)
        return res