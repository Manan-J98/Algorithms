class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()

        s, e = 0, 0
        maxOverlap = 0
        ongoing = 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                ongoing += 1
                s += 1
            else:
                ongoing -= 1
                e += 1
            maxOverlap = max(maxOverlap, ongoing)
        return maxOverlap