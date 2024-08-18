import unittest

from problems.intervals.meeting_rooms_ii import MeetingRoomsII


class TestMeetingRoomsII(unittest.TestCase):

    def setUp(self):
        self.meeting_rooms = MeetingRoomsII()

    def test_min_meeting_rooms(self):
        # Test case: Overlapping intervals
        intervals1 = [[0, 30], [5, 10], [15, 20]]
        self.assertEqual(self.meeting_rooms.minMeetingRooms(intervals1), 2)

        # Test case: Non-overlapping intervals
        intervals2 = [[7, 10], [2, 4]]
        self.assertEqual(self.meeting_rooms.minMeetingRooms(intervals2), 1)

        # Test case: Single interval
        intervals3 = [[1, 5]]
        self.assertEqual(self.meeting_rooms.minMeetingRooms(intervals3), 1)

        # Test case: Empty intervals array
        intervals4 = []
        self.assertEqual(self.meeting_rooms.minMeetingRooms(intervals4), 0)

        # Test case: Null intervals array
        intervals5 = None
        # noinspection PyTypeChecker
        self.assertEqual(self.meeting_rooms.minMeetingRooms(intervals5), 0)

        # Test case: Multiple meetings at the same time
        intervals6 = [[1, 10], [1, 10], [1, 10]]
        self.assertEqual(self.meeting_rooms.minMeetingRooms(intervals6), 3)


if __name__ == '__main__':
    unittest.main()
