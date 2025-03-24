class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_days = 0
        prev_end = 0

        for start, end in meetings:
            if start > prev_end + 1:
                free_days += start - prev_end - 1
            prev_end = max(prev_end, end)

        # Account for any free days after the last meeting
        if prev_end < days:
            free_days += days - prev_end

        return free_days
