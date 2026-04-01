import unittest

class TestFileHasher(unittest.TestCase):
    def setUp(self):
        self.hasher = FileHasher()

    def test_hash_string(self):
        text = "Hello, World!"
        expected_hash = "dffd9060343b089c166884f276f855597264b84d6551f495c794674c43e099c"
        self.assertEqual(self.hasher.hash_string(text), expected_hash)

    def test_check_integrity(self):
        text = "Hello, World!"
        expected_hash = "dffd9060343b089c166884f276f855597264b84d6551f495c794674c43e099c"
        self.assertTrue(self.hasher.check_integrity(text, expected_hash))

    def test_check_integrity_failure(self):
        text = "Hello, World!"
        expected_hash = "dffd9060343b089c166884f276f855597264b84d6551f495c794674c43e099d"
        self.assertFalse(self.hasher.check_integrity(text, expected_hash))

if __name__ == '__main__':
    unittest.main()
