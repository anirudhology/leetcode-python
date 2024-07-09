import unittest

from problems.string.encode_and_decode_strings import EncodeAndDecodeStrings


class EncodeAndDecodeStringsTest(unittest.TestCase):

    def setUp(self):
        self.encoder_decoder = EncodeAndDecodeStrings()

    def test_encode_single_word(self):
        strs = ["hello"]
        encoded = self.encoder_decoder.encode(strs)
        self.assertEqual(encoded, "5/hello")

    def test_decode_single_word(self):
        encoded = "5/hello"
        decoded = self.encoder_decoder.decode(encoded)
        self.assertEqual(decoded, ["hello"])

    def test_encode_multiple_words(self):
        strs = ["hello", "world"]
        encoded = self.encoder_decoder.encode(strs)
        self.assertEqual(encoded, "5/hello5/world")

    def test_decode_multiple_words(self):
        encoded = "5/hello5/world"
        decoded = self.encoder_decoder.decode(encoded)
        self.assertEqual(decoded, ["hello", "world"])

    def test_encode_empty_string(self):
        strs = [""]
        encoded = self.encoder_decoder.encode(strs)
        self.assertEqual(encoded, "0/")

    def test_decode_empty_string(self):
        encoded = "0/"
        decoded = self.encoder_decoder.decode(encoded)
        self.assertEqual(decoded, [""])

    def test_encode_mixed_strings(self):
        strs = ["hello", "", "world"]
        encoded = self.encoder_decoder.encode(strs)
        self.assertEqual(encoded, "5/hello0/5/world")

    def test_decode_mixed_strings(self):
        encoded = "5/hello0/5/world"
        decoded = self.encoder_decoder.decode(encoded)
        self.assertEqual(decoded, ["hello", "", "world"])

    def test_encode_special_characters(self):
        strs = ["hello/world", "foo/bar"]
        encoded = self.encoder_decoder.encode(strs)
        self.assertEqual(encoded, "11/hello/world7/foo/bar")

    def test_decode_special_characters(self):
        encoded = "11/hello/world7/foo/bar"
        decoded = self.encoder_decoder.decode(encoded)
        self.assertEqual(decoded, ["hello/world", "foo/bar"])

    def test_encode_empty_list(self):
        strs = []
        encoded = self.encoder_decoder.encode(strs)
        self.assertEqual(encoded, "")

    def test_decode_empty_string_to_list(self):
        encoded = ""
        decoded = self.encoder_decoder.decode(encoded)
        self.assertEqual(decoded, [])


if __name__ == "__main__":
    unittest.main()
