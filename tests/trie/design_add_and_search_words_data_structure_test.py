import unittest

from problems.trie.design_add_and_search_words_data_structure import WordDictionary


class TestWordDictionary(unittest.TestCase):

    def setUp(self):
        self.wordDictionary = WordDictionary()

    def test_add_word_and_search(self):
        self.wordDictionary.addWord("apple")
        self.assertTrue(self.wordDictionary.search("apple"))
        self.assertFalse(self.wordDictionary.search("app"))
        self.assertFalse(self.wordDictionary.search("a.le"))
        self.assertTrue(self.wordDictionary.search("a.ple"))

    def test_add_word_with_prefix(self):
        self.wordDictionary.addWord("car")
        self.wordDictionary.addWord("card")
        self.assertTrue(self.wordDictionary.search("car"))
        self.assertTrue(self.wordDictionary.search("card"))
        self.assertFalse(self.wordDictionary.search("ca"))
        self.assertTrue(self.wordDictionary.search("c.r"))

    def test_search_with_wildcard(self):
        self.wordDictionary.addWord("bat")
        self.wordDictionary.addWord("ball")
        self.assertTrue(self.wordDictionary.search("b.t"))
        self.assertTrue(self.wordDictionary.search("ba.l"))
        self.assertTrue(self.wordDictionary.search("b..l"))
        self.assertFalse(self.wordDictionary.search("b..m"))

    def test_add_duplicate_word(self):
        self.wordDictionary.addWord("dog")
        self.wordDictionary.addWord("dog")
        self.assertTrue(self.wordDictionary.search("dog"))

    def test_add_empty_word(self):
        self.wordDictionary.addWord("")
        self.assertTrue(self.wordDictionary.search(""))
        self.assertFalse(self.wordDictionary.search("."))

    def test_search_empty_trie(self):
        self.assertFalse(self.wordDictionary.search("anything"))

    def test_search_with_wildcard_only(self):
        self.wordDictionary.addWord("cat")
        self.assertTrue(self.wordDictionary.search("..."))
        self.assertFalse(self.wordDictionary.search(".."))

    def test_add_word_with_all_characters(self):
        all_chars = "abcdefghijklmnopqrstuvwxyz"
        self.wordDictionary.addWord(all_chars)
        self.assertTrue(self.wordDictionary.search(all_chars))
        self.assertFalse(self.wordDictionary.search(all_chars + "a"))


if __name__ == '__main__':
    unittest.main()
