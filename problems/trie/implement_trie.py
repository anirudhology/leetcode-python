from problems.util.trie_node import TrieNode


class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        # Check if the word is already present
        if self.search(word):
            return
        current = self.root
        for c in word:
            if not current.children[ord(c) - ord('a')]:
                current.children[ord(c) - ord('a')] = TrieNode(c)
            current = current.children[ord(c) - ord('a')]
        current.isWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if not current.children[ord(c) - ord('a')]:
                return False
            current = current.children[ord(c) - ord('a')]
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if not current.children[ord(c) - ord('a')]:
                return False
            current = current.children[ord(c) - ord('a')]
        return True
