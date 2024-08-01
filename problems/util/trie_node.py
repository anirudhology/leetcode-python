class TrieNode:
    def __init__(self, content):
        self.content = content
        self.children = [None] * 26
        self.isWord = False
