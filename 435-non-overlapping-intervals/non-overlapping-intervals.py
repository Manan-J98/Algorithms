class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        i = 1
        while i < len(intervals):
            # if overlapping
            if prevEnd > intervals[i][0]:
                count += 1
                prevEnd = min(intervals[i][1], prevEnd)
            else:
                prevEnd = intervals[i][1]
            i += 1
        return count