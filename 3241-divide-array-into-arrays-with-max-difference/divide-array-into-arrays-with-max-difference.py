class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i])
            if len(temp) == 3:
                res.append(temp)
                temp = []
        for first, _, last in res:
            if last - first > k:
                return []
        return res