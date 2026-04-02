from subject_38 import *

import unittest

def entance(side_length):
    if isinstance(side_length, (int, float)) and side_length > 0:
        area = (3**0.5 * side_length**2) / 4
        return round(area, 2)
    else:
        return "Invalid input value for side length"

class TestEntance(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(entance(2), 1.73)
        self.assertEqual(entance(3), 3.89)
        self.assertEqual(entance(5), 10.83)
    
    def test_negative_input(self):
        self.assertEqual(entance(-1), "Invalid input value for side length")
    
    def test_zero_input(self):
        self.assertEqual(entance(0), "Invalid input value for side length")
    
    def test_non_numeric_input(self):
        self.assertEqual(entance("a"), "Invalid input value for side length")
        self.assertEqual(entance(None), "Invalid input value for side length")
        self.assertEqual(entance([]), "Invalid input value for side length")
        self.assertEqual(entance({}), "Invalid input value for side length")

if __name__ == '__main__':
    unittest.main()