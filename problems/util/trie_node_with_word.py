from typing import List, Optional


class TrieNodeWithWord:
    def __init__(self):
        self.word = None
        self.children: List[Optional['TrieNodeWithWord']] = [None] * 26
