import unittest

class TestParseMusicFunction(unittest.TestCase):

    # Test case for the given example in the problem description
    def test_example(self):
        input_string = "o o| .| o| o| .| o| o| .| .| o| .| .| .| o|"
        expected_output = [4, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2]
        self.assertEqual(parse_music(input_string), expected_output)

    # Test case for a simple input
    def test_simple_input(self):
        input_string = "o o| .|"
        expected_output = [4, 2, 1]
        self.assertEqual(parse_music(input_string), expected_output)

    # Test case for a single note
    def test_single_note(self):
        input_string = "o"
        expected_output = [4]
        self.assertEqual(parse_music(input_string), expected_output)

    # Test case for multiple notes of the same type
    def test_multiple_notes_same_type(self):
        input_string = "o o o o"
        expected_output = [4, 4, 4, 4]
        self.assertEqual(parse_music(input_string), expected_output)

    # Test case for an empty string
    def test_empty_string(self):
        input_string = ""
        expected_output = []
        self.assertEqual(parse_music(input_string), expected_output)

    # Test case for a string with invalid notes
    def test_invalid_notes(self):
        input_string = "o o| .| o| o| x| .| o| o| .| .| o| .| .| .| o|"
        expected_output = [4, 2, 1, 2, 2, 0, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2]
        self.assertEqual(parse_music(input_string), expected_output)