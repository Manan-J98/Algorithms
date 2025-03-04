class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res = []
        heapify(nums)
        while nums:
            alice, bob = heappop(nums), heappop(nums)
            res.append(bob)
            res.append(alice)
        return res