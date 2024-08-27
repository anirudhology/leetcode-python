from typing import List


class DetectSquares:

    def __init__(self):
        self.coordinates = []
        self.frequencies = {}

    def add(self, point: List[int]) -> None:
        self.coordinates.append(point)
        key = str(point[0]) + "," + str(point[1])
        if key in self.frequencies:
            self.frequencies[key] += 1
        else:
            self.frequencies[key] = 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        result = 0
        for coordinate in self.coordinates:
            px, py = coordinate[0], coordinate[1]
            if abs(px - x) == abs(py - y) and px != x and py != y:
                key_1 = str(x) + "," + str(py)
                key_2 = str(px) + "," + str(y)
                count = 1
                if key_1 in self.frequencies:
                    count *= self.frequencies[key_1]
                else:
                    count = 0
                if key_2 in self.frequencies:
                    count *= self.frequencies[key_2]
                else:
                    count = 0
                result += count
        return result
