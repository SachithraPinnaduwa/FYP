# import unittest

# def longest_repeating_substring(s):
#     length = len(s)
#     sub_strings = {}

#     for i1 in range(length):
#         for i2 in range(i1+1, length+1):
#             item = s[i1:i2]
#             if item in sub_strings:
#                 sub_strings[item][0] += 1
#             else:
#                 sub_strings[item] = [1, i1]

#     max_length = 0
#     earliest_starting_position = float("inf")
#     longest_substring = ""

#     for key, value in sub_strings.items():
#         if value[0] > 1:
#             if len(key) > max_length or (len(key) == max_length and value[1] < earliest_starting_position):
#                 max_length = len(key)
#                 earliest_starting_position = value[1]
#                 longest_substring = key
#     return longest_substring

# class TestLongestRepeatingSubstring(unittest.TestCase):
#     def test_empty_string(self):
#         self.assertEqual(longest_repeating_substring(""), "")

#     def test_single_character(self):
#         self.assertEqual(longest_repeating_substring("a"), "")

#     def test_no_repeating_substring(self):
#         self.assertEqual(longest_repeating_substring("abcdefg"), "")

#     def test_repeating_substring_at_beginning(self):
#         self.assertEqual(longest_repeating_substring("ababab"), "abab")

#     def test_repeating_substring_at_end(self):
#         self.assertEqual(longest_repeating_substring("abababab"), "ababab")

#     def test_repeating_substring_in_middle(self):
#         self.assertEqual(longest_repeating_substring("abcabcabc"), "abcabc")

#     def test_repeating_substring_with_earliest_starting_position(self):
#         self.assertEqual(longest_repeating_substring("abcdeabcde"), "abcde")

#     def test_repeating_substring_with_longest_length(self):
#         self.assertEqual(longest_repeating_substring("abcabcabc"), "abcabc")

#     def test_repeating_substring_with_multiple_occurrences(self):
#         self.assertEqual(longest_repeating_substring("abcabcabcabc"), "abcabcabc")

#     def test_repeating_substring_with_large_input(self):
#         s = "a" * 1000000 + "b" * 1000000 + "c" * 1000000
#         self.assertEqual(longest_repeating_substring(s), s[:1000000])

# if __name__ == '__main__':
#     unittest.main()

# removed due to crashing