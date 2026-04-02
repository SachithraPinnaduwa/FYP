import unittest

class TestCheckSubstring(unittest.TestCase):
    def test_check_substring(self):
        self.assertTrue(check_substring("Hello, world!", "world"))
        self.assertFalse(check_substring("Hello, world!", "Python"))
        self.assertTrue(check_substring("Hello, world!", "hello"))
        self.assertFalse(check_substring("Hello, world!", "Hello,"))
        self.assertTrue(check_substring("Hello, world!", "orld"))
        self.assertFalse(check_substring("Hello, world!", "world! "))

if __name__ == '__main__':
    unittest.main()