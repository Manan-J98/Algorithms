class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]: # can inclue in one range
                res[-1][1] = max(intervals[i][1], res[-1][1]) # right max range could be either
            else:
                res.append(intervals[i])
        return res
            
        