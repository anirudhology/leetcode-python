import heapq
from collections import Counter
from typing import List


class HandOfStraights:
    @staticmethod
    def isNStraightHand(hand: List[int], groupSize: int) -> bool:
        # Count the occurrences of keys
        count = Counter(hand)
        # Min heap to store all elements
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        # Process all the cards
        while min_heap:
            first_card = min_heap[0]
            for i in range(groupSize):
                current_card = first_card + i
                # Check if this card is present
                if count[current_card] == 0:
                    return False
                count[current_card] -= 1
                if count[current_card] == 0:
                    if current_card != min_heap[0]:
                        return False
                    # Remove from heap if count drops to 0
                    heapq.heappop(min_heap)
        return True
