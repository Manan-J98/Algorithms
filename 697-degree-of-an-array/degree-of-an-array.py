class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        degree = max(freq.values())
        res = float('inf')
        for key, val in freq.items():
            if val == degree:
                fp, sp = None, None
                for index, num in enumerate(nums):
                    if (fp == None) and (sp == None) and num == key:
                        print(index)
                        fp = index
                        sp = index
                    elif num == key and not (fp == None):
                        sp = index
                print(fp, sp)
                res = min(res, sp-fp+1)
        return res

