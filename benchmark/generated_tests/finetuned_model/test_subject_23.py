import unittest

class TestEntranceFunction(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(entrance("listen", "silent"))
        self.assertTrue(entrance("triangle", "integral"))
        self.assertTrue(entrance("night", "thing"))
        self.assertTrue(entrance("earth", "heart"))
        self.assertTrue(entrance("star", "rats"))

    def test_not_anagrams(self):
        self.assertFalse(entrance("hello", "world"))
        self.assertFalse(entrance("python", "java"))
        self.assertFalse(entrance("test", "ttew"))
        self.assertFalse(entrance("abc", "def"))
        self.assertFalse(entrance("racecar", "carrace"))

    def test_case_insensitivity(self):
        self.assertTrue(entrance("Listen", "Silent"))
        self.assertTrue(entrance("Racecar", "Car race"))
        self.assertTrue(entrance("Dormitory", "Dirty room"))

    def test_whitespace_ignored(self):
        self.assertTrue(entrance("a man", "nma"))
        self.assertTrue(entrance("a  man", "nma"))
        self.assertTrue(entrance("a man ", "nma"))
        self.assertTrue(entrance("a  man ", "nma"))

if __name__ == '__main__':
    unittest.main()