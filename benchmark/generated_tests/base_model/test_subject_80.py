import unittest

class TestCheckSubstring(unittest.TestCase):
    def test_check_substring(self):
        self.assertTrue(check_substring("Hello World", "world"))
        self.assertFalse(check_substring("Python Programming", "java"))
        self.assertTrue(check_substring("Case Insensitive", "sensit"))
        self.assertFalse(check_substring("Mismatch", "Match"))
        self.assertTrue(check_substring("Repetition", "pete"))
        self.assertFalse(check_substring("Empty Base String", ""))
        self.assertFalse(check_substring("", "Non Empty Substring"))
        self.assertTrue(check_substring("Single Character", "c"))
        self.assertFalse(check_substring("One Word", "Two Words"))

if __name__ == '__main__':
    unittest.main()