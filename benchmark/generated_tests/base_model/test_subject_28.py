import unittest

class TestLongestRepeatingSubstring(unittest.TestCase):

    def test_longest_repeating_substring(self):
        self.assertEqual(longest_repeating_substring("banana"), "ana")
        self.assertEqual(longest_repeating_substring("abcd"), "")
        self.assertEqual(longest_repeating_substring("aabbccdd"), "ab")
        self.assertEqual(longest_repeating_substring("abcabcabc"), "abc")
        self.assertEqual(longest_repeating_substring("abcdeffedcba"), "fedcb")
        self.assertEqual(longest_repeating_substring("aaaa"), "aa")
        self.assertEqual(longest_repeating_substring(""), "")
        self.assertEqual(longest_repeating_substring("abcdefg"), "")

if __name__ == '__main__':
    unittest.main()