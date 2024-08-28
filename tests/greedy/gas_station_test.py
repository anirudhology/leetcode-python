import unittest

from problems.greedy.gas_station import GasStation


class TestGasStation(unittest.TestCase):

    def test_can_complete_circuit_basic(self):
        gas_station = GasStation()
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        self.assertEqual(gas_station.canCompleteCircuit(gas, cost), 3)

    def test_can_complete_circuit_no_solution(self):
        gas_station = GasStation()
        gas = [2, 3, 4]
        cost = [3, 4, 5]
        self.assertEqual(gas_station.canCompleteCircuit(gas, cost), -1)

    def test_can_complete_circuit_single_station(self):
        gas_station = GasStation()
        gas = [5]
        cost = [4]
        self.assertEqual(gas_station.canCompleteCircuit(gas, cost), 0)

    def test_can_complete_circuit_all_stations_equal(self):
        gas_station = GasStation()
        gas = [1, 1, 1, 1]
        cost = [1, 1, 1, 1]
        self.assertEqual(gas_station.canCompleteCircuit(gas, cost), 0)

    def test_can_complete_circuit_multiple_solutions(self):
        gas_station = GasStation()
        gas = [2, 3, 4]
        cost = [2, 1, 2]
        self.assertEqual(gas_station.canCompleteCircuit(gas, cost), 0)  # Returns the first valid start


if __name__ == '__main__':
    unittest.main()
