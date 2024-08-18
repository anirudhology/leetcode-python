from typing import List


class MeetingRoomsII:
    @staticmethod
    def minMeetingRooms(intervals: List[List[int]]) -> int:
        # Special case
        if intervals is None or len(intervals) == 0:
            return 0
        # Total number of intervals
        n = len(intervals)
        # Lists to store start and end times
        start_times = [0] * n
        end_times = [0] * n
        for i in range(n):
            start_times[i] = intervals[i][0]
            end_times[i] = intervals[i][1]
        # Sort both arrays
        start_times.sort()
        end_times.sort()
        # Required meeting rooms
        required_meeting_rooms = 0
        # Meetings in progress
        meetings_in_progress = 0
        # Pointers for start and end times
        start, end = 0, 0
        while start < n:
            if start_times[start] < end_times[end]:
                start += 1
                meetings_in_progress += 1
            else:
                end += 1
                meetings_in_progress -= 1
            required_meeting_rooms = max(required_meeting_rooms, meetings_in_progress)
        return required_meeting_rooms
