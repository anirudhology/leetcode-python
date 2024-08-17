import unittest

from problems.intervals.meeting_rooms import MeetingRooms


class TestMeetingRooms(unittest.TestCase):

    def setUp(self):
        self.meeting_rooms = MeetingRooms()

    def test_can_attend_all_meetings(self):
        # Test case: No overlapping intervals
        intervals1 = [[0, 30], [35, 50], [60, 75]]
        self.assertTrue(self.meeting_rooms.canAttendMeetings(intervals1))

        # Test case: Overlapping intervals
        intervals2 = [[0, 30], [20, 50], [60, 75]]
        self.assertFalse(self.meeting_rooms.canAttendMeetings(intervals2))

        # Test case: Empty array
        intervals3 = []
        self.assertTrue(self.meeting_rooms.canAttendMeetings(intervals3))

        # Test case: Single interval
        intervals4 = [[10, 20]]
        self.assertTrue(self.meeting_rooms.canAttendMeetings(intervals4))

        # Test case: Continuous but non-overlapping intervals
        intervals5 = [[0, 10], [10, 20], [20, 30]]
        self.assertTrue(self.meeting_rooms.canAttendMeetings(intervals5))


if __name__ == '__main__':
    unittest.main()
