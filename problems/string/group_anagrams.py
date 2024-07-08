from typing import List


class GroupAnagrams:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        # List to store the final output
        groups = []
        # Special case
        if strs is None or len(strs) == 0:
            return groups
        # Dictionary to store the frequency representation of words
        # and the words themselves
        mappings = {}
        # Process each string one by one
        for s in strs:
            # List to store frequency representation of the current word
            frequency = [0] * 26
            for c in s:
                frequency[ord(c) - ord("a")] += 1
            key = str(frequency)
            # Add the key value pair
            if key not in mappings:
                mappings[key] = []
            mappings[key].append(s)
        # Finally iterate over the mappings and get all groups
        for group in mappings.values():
            groups.append(group)
        return groups
