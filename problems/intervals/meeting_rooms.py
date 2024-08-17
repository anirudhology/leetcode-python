from typing import List


class MeetingRooms:
    @staticmethod
    def canAttendMeetings(intervals: List[List[int]]) -> bool:
        # Sort all intervals by their start time
        intervals.sort(key=lambda x: x[0])
        # Process all intervals
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False

        return True
