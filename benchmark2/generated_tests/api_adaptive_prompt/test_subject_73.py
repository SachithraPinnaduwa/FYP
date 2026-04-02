from subject_73 import *

import unittest

def entrance(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:  
            for i in range(2, num):
                if (num % i) == 0:  
                    break
            else:
                primes.append(num)  
    return primes

class TestEntranceFunction(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(entrance(1, 10), [2, 3, 5, 7])

    def test_edge_case_single_number(self):
        self.assertEqual(entrance(2, 2), [2])

    def test_edge_case_empty_range(self):
        self.assertEqual(entrance(0, 1), [])

    def test_error_handling_negative_start(self):
        self.assertEqual(entrance(-5, 5), [])

    def test_error_handling_non_integer_start(self):
        with self.assertRaises(TypeError):
            entrance(2.5, 5)

if __name__ == '__main__':
    unittest.main()