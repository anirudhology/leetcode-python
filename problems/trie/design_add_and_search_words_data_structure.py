from problems.util.trie_node import TrieNode


class WordDictionary:

    def __init__(self):
        self.root = TrieNode('')

    def addWord(self, word: str) -> None:
        if self.search(word):
            return
        current = self.root
        for c in word:
            if not current.children[ord(c) - ord('a')]:
                current.children[ord(c) - ord('a')] = TrieNode(c)
            current = current.children[ord(c) - ord('a')]
        current.isWord = True

    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.root)

    def search_helper(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.isWord
        if word[index] == '.':
            for child in node.children:
                if child and self.search_helper(word, index + 1, child):
                    return True
        else:
            return node.children[ord(word[index]) - ord('a')] and self.search_helper(word, index + 1, node.children[
                ord(word[index]) - ord('a')])
