import unittest

from problems.graph.reconstruct_itinerary import ReconstructItinerary


class TestReconstructItinerary(unittest.TestCase):
    def test_find_itinerary(self):
        reconstruct_itinerary = ReconstructItinerary()

        # Test case 1
        tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        expected1 = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        self.assertEqual(reconstruct_itinerary.findItinerary(tickets1), expected1)

        # Test case 2
        tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        expected2 = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        self.assertEqual(reconstruct_itinerary.findItinerary(tickets2), expected2)


if __name__ == "__main__":
    unittest.main()
