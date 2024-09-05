from collections import deque
from typing import List


class AlienDictionary:
    @staticmethod
    def foreignDictionary(words: List[str]) -> str:
        # Total number of words
        n = len(words)
        # Graph to represent the order among characters
        graph = [[False] * 26 for _ in range(26)]
        # Characters that are present in the words
        characters = [False] * 26
        # Count of unique characters in the dictionary
        unique_character_count = 0
        # Process the words to fill up characters array
        for word in words:
            for c in word:
                if unique_character_count == 26:
                    break
                index = ord(c) - ord('a')
                if not characters[index]:
                    characters[index] = True
                    unique_character_count += 1

        # Populate the graph
        for i in range(n - 1):
            for j in range(len(words[i])):
                # If next word is a prefix of current word then
                # we have an invalid order
                if j >= len(words[i + 1]):
                    return ""
                # Compare characters of two consecutive words
                current_character, next_character = words[i][j], words[i + 1][j]
                # If these characters are same then we don't get any information
                # about the order
                if current_character == next_character:
                    continue
                x, y = ord(current_character) - ord('a'), ord(next_character) - ord('a')
                # If there is already a directed edge between next_character
                # and current_character, then we have a cycle in the graph
                if graph[y][x]:
                    return ""
                # Create an edge between current_character and next_character
                graph[x][y] = True
                break

        # Since the graph is created, we will perform topological sorting

        # 1. Array to store indegrees of nodes
        indegrees = [0] * 26
        for i in range(26):
            for j in range(26):
                if i != j and characters[i] and characters[j] and graph[i][j]:
                    indegrees[j] += 1

        # 2. Queue to store nodes with zero indegree
        nodes = deque()
        for i in range(26):
            if characters[i] and indegrees[i] == 0:
                nodes.append(i)

        # 3. Perform topological sorting
        order = []
        while nodes:
            current = nodes.popleft()
            order.append(chr(current + ord('a')))
            for i in range(26):
                if i != current and characters[i] and graph[current][i]:
                    indegrees[i] -= 1
                    if indegrees[i] == 0:
                        nodes.append(i)

        return "" if len(order) < unique_character_count else "".join(order)
