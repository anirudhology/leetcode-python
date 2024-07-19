import unittest

from problems.binary_search.time_based_key_value_store import TimeMap


class TestTimeMap(unittest.TestCase):

    def setUp(self):
        self.time_map = TimeMap()

    def test_set_and_get(self):
        self.time_map.set("foo", "bar", 1)
        self.assertEqual(self.time_map.get("foo", 1), "bar")
        self.assertEqual(self.time_map.get("foo", 2), "bar")

        self.time_map.set("foo", "bar2", 4)
        self.assertEqual(self.time_map.get("foo", 4), "bar2")
        self.assertEqual(self.time_map.get("foo", 5), "bar2")

    def test_get_nonexistent_key(self):
        self.assertEqual(self.time_map.get("nonexistent", 1), "")

    def test_get_with_no_set_operations(self):
        self.assertEqual(self.time_map.get("foo", 1), "")

    def test_multiple_keys(self):
        self.time_map.set("foo", "bar", 1)
        self.time_map.set("baz", "qux", 2)
        self.assertEqual(self.time_map.get("foo", 1), "bar")
        self.assertEqual(self.time_map.get("baz", 2), "qux")

    def test_set_multiple_times_same_key(self):
        self.time_map.set("foo", "bar", 1)
        self.time_map.set("foo", "bar2", 2)
        self.time_map.set("foo", "bar3", 3)
        self.assertEqual(self.time_map.get("foo", 2), "bar2")
        self.assertEqual(self.time_map.get("foo", 3), "bar3")
        self.assertEqual(self.time_map.get("foo", 4), "bar3")

    def test_edge_case_empty_key(self):
        self.time_map.set("", "empty", 1)
        self.assertEqual(self.time_map.get("", 1), "empty")
        self.assertEqual(self.time_map.get("", 2), "empty")

    def test_edge_case_empty_value(self):
        self.time_map.set("foo", "", 1)
        self.assertEqual(self.time_map.get("foo", 1), "")
        self.assertEqual(self.time_map.get("foo", 2), "")

    def test_timestamp_order(self):
        self.time_map.set("foo", "bar1", 1)
        self.time_map.set("foo", "bar2", 2)
        self.time_map.set("foo", "bar3", 3)
        self.assertEqual(self.time_map.get("foo", 1), "bar1")
        self.assertEqual(self.time_map.get("foo", 2), "bar2")
        self.assertEqual(self.time_map.get("foo", 3), "bar3")
        self.assertEqual(self.time_map.get("foo", 4), "bar3")


if __name__ == '__main__':
    unittest.main()
