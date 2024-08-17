import heapq
from collections import Counter, deque
from typing import List


class TaskScheduler:
    @staticmethod
    def leastInterval(tasks: List[str], n: int) -> int:
        # Special case
        if not tasks:
            return 0
        # Calculate frequencies of the tasks
        frequencies = Counter(tasks)
        # Max heap to store frequencies (negating to use min-heap as max-heap)
        max_heap = [-frequency for frequency in frequencies.values()]
        heapq.heapify(max_heap)
        # Queue to store pairs of frequency of a task and the time it can be executed again
        pairs = deque()
        # Total time to execute all tasks
        time = 0
        # Process the tasks
        while max_heap or pairs:
            time += 1
            if not max_heap:
                time = pairs[0][1]
            else:
                frequency = 1 + heapq.heappop(max_heap)
                if frequency:
                    pairs.append([frequency, time + n])
            if pairs and pairs[0][1] == time:
                heapq.heappush(max_heap, pairs.popleft()[0])
        return time
