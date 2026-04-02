import unittest

class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("triangle", "integral"))
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))
        self.assertTrue(is_anagram("dormitory", "dirty room"))
        self.assertFalse(is_anagram("conversation", "voices rant on"))
        self.assertTrue(is_anagram("school master", "the classroom"))
        self.assertFalse(is_anagram("astronomer", "moon starer"))
        self.assertTrue(is_anagram("conversation", "voices rant on"))
        self.assertFalse(is_anagram("astronomer", "moon starer"))

if __name__ == '__main__':
    unittest.main()