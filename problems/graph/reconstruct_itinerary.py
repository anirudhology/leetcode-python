import heapq
from collections import defaultdict, deque
from typing import List


class ReconstructItinerary:
    @staticmethod
    def findItinerary(tickets: List[List[str]]) -> List[str]:
        # Since we need to return the path in lexical order, we will
        # use minHeap to store airports. Thus, we need a map that will
        # connect the departure and arrival airports
        flights = defaultdict(list)
        # List to store the final path
        path = deque()
        # Process all flights to create the mappings
        for departure, arrival in tickets:
            heapq.heappush(flights[departure], arrival)

        def dfs(departure_airport):
            while flights[departure_airport]:
                dfs(heapq.heappop(flights[departure_airport]))
            path.appendleft(departure_airport)

        # We start from JFK, hence we will perform DFS from there
        dfs("JFK")
        return list(path)
