import unittest

from problems.trie.implement_trie import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        # Test inserting and searching single word
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))  # should return True
        self.assertFalse(self.trie.search("app"))  # should return False
        self.assertTrue(self.trie.startsWith("app"))  # should return True

        # Test inserting word which is a prefix of another word
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"))  # should return True

    def test_starts_with(self):
        # Test startsWith for different prefixes
        self.trie.insert("banana")
        self.assertTrue(self.trie.startsWith("ban"))  # should return True
        self.assertTrue(self.trie.startsWith("bana"))  # should return True
        self.assertFalse(self.trie.startsWith("bananaa"))  # should return False

        # Test startsWith for non-existing prefix
        self.assertFalse(self.trie.startsWith("xyz"))  # should return False

    def test_insert_duplicate_words(self):
        # Test inserting the same word multiple times
        self.trie.insert("car")
        self.trie.insert("car")
        self.trie.insert("car")
        self.assertTrue(self.trie.search("car"))  # should return True

        # Test startsWith after inserting duplicates
        self.assertTrue(self.trie.startsWith("ca"))  # should return True

    def test_empty_string(self):
        # Test inserting and searching empty string
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))  # should return True
        self.assertTrue(self.trie.startsWith(""))  # should return True


if __name__ == "__main__":
    unittest.main()
