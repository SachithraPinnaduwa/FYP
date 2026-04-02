import unittest

class TestCheckSubstring(unittest.TestCase):
    def test_case_1(self):
        # Test case 1: Substring is present
        self.assertTrue(check_substring("Hello World", "world"))
    
    def test_case_2(self):
        # Test case 2: Substring is not present
        self.assertFalse(check_substring("Hello World", "universe"))
    
    def test_case_3(self):
        # Test case 3: Case-insensitive substring
        self.assertTrue(check_substring("Hello World", "WORLD"))
    
    def test_case_4(self):
        # Test case 4: Substring is the same as the base string
        self.assertTrue(check_substring("Hello World", "Hello World"))
    
    def test_case_5(self):
        # Test case 5: Substring is an empty string
        self.assertTrue(check_substring("Hello World", ""))
    
    def test_case_6(self):
        # Test case 6: Substring is longer than the base string
        self.assertFalse(check_substring("Hello World", "Hello World Extra"))
    
    def test_case_7(self):
        # Test case 7: Substring is a single character
        self.assertTrue(check_substring("Hello World", "o"))
    
    def test_case_8(self):
        # Test case 8: Substring is a single character not present
        self.assertFalse(check_substring("Hello World", "z"))
    
    def test_case_9(self):
        # Test case 9: Substring is a substring of the base string
        self.assertTrue(check_substring("Hello World", "lo"))
    
    def test_case_10(self):
        # Test case 10: Substring is a substring of the base string (case-insensitive)
        self.assertTrue(check_substring("Hello World", "LO"))

if __name__ == '__main__':
    unittest.main()
