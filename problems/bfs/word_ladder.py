from collections import deque
from string import ascii_lowercase
from typing import List


class WordLadder:
    @staticmethod
    def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert the list to set for O(1) search
        words = set(wordList)
        # Check if endWord is not in set of words
        if endWord not in words:
            return 0
        # Queue to perform BFS
        nodes = deque([beginWord])
        # Since we are starting from beginWord, we are at
        # the first rung of the ladder
        level = 1
        # Process until the queue is empty or the endWord is found
        while nodes:
            size = len(nodes)
            for i in range(size):
                # Get the current word
                currentWord = list(nodes.popleft())
                # Check for every character in the currentWord
                for j in range(len(currentWord)):
                    originalCharacter = currentWord[j]
                    # Try for every alphabet
                    for c in ascii_lowercase:
                        currentWord[j] = c
                        currentWordString = ''.join(currentWord)
                        # Check if this currentWord is present in the set
                        if currentWordString in words:
                            if endWord == currentWordString:
                                return level + 1
                            words.remove(currentWordString)
                            nodes.append(currentWordString)
                    # Restore the original word
                    currentWord[j] = originalCharacter
            level += 1
        return 0
