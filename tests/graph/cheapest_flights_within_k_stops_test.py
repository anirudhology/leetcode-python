import unittest

from problems.graph.cheapest_flights_within_k_stops import CheapestFlightsWithinKStops


class TestCheapestFlightsWithinKStops(unittest.TestCase):

    def test_basic_scenario(self):
        cheapest_flight_within_k_flights = CheapestFlightsWithinKStops()
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        result = cheapest_flight_within_k_flights.findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, 200)

    def test_no_available_flight(self):
        cheapest_flight_within_k_flights = CheapestFlightsWithinKStops()
        n = 3
        flights = [[0, 1, 100]]
        src = 0
        dst = 2
        k = 1
        result = cheapest_flight_within_k_flights.findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, -1)

    def test_direct_flight(self):
        cheapest_flight_within_k_flights = CheapestFlightsWithinKStops()
        n = 3
        flights = [[0, 2, 300]]
        src = 0
        dst = 2
        k = 1
        result = cheapest_flight_within_k_flights.findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, 300)

    def test_no_stop_allowed(self):
        cheapest_flight_within_k_flights = CheapestFlightsWithinKStops()
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        result = cheapest_flight_within_k_flights.findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, 500)

    def test_large_k_value(self):
        cheapest_flight_within_k_flights = CheapestFlightsWithinKStops()
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 3, 500]]
        src = 0
        dst = 3
        k = 2
        result = cheapest_flight_within_k_flights.findCheapestPrice(n, flights, src, dst, k)
        self.assertEqual(result, 300)


if __name__ == '__main__':
    unittest.main()
