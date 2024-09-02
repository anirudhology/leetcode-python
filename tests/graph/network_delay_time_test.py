import unittest

from problems.graph.network_delay_time import NetworkDelayTime


class TestNetworkDelayTime(unittest.TestCase):

    def setUp(self):
        self.network_delay_time = NetworkDelayTime()

    def test_network_delay_time(self):
        # Test case 1: Basic case with all nodes reachable
        self.assertEqual(self.network_delay_time.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2)

        # Test case 2: Node unreachable
        self.assertEqual(self.network_delay_time.networkDelayTime([[1, 2, 1]], 2, 1), 1)

        # Test case 3: Single node, self delay is 0
        self.assertEqual(self.network_delay_time.networkDelayTime([], 1, 1), 0)

        # Test case 4: All nodes connected in a line
        self.assertEqual(self.network_delay_time.networkDelayTime([[1, 2, 1], [2, 3, 1], [3, 4, 1]], 4, 1), 3)

        # Test case 5: Empty times array, unreachable nodes
        self.assertEqual(self.network_delay_time.networkDelayTime([], 2, 1), -1)

        # Test case 6: Cycle in the graph
        self.assertEqual(self.network_delay_time.networkDelayTime([[1, 2, 1], [2, 3, 2], [3, 1, 3]], 3, 1), 3)


if __name__ == '__main__':
    unittest.main()
