from subject_37 import *

import unittest

class TestFindSecondSmallestOddPrimeGreaterThan100(unittest.TestCase):
    def test_find_second_smallest_odd_prime_greater_than_100(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 103, 105, 107, 109, 111, 113]), 103)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([115, 117, 119, 121, 123, 125, 127]), 119)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([129, 131, 133, 135, 137, 139, 141]), 131)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([143, 145, 147, 149, 151, 153, 155]), 149)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([157, 159, 161, 163, 165, 167, 169]), 161)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([171, 173, 175, 177, 179, 181, 183]), 173)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([185, 187, 189, 191, 193, 195, 197]), 189)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([199, 201, 203, 205, 207, 209, 211]), 201)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([213, 215, 217, 219, 221, 223, 225]), 217)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([227, 229, 231, 233, 235, 237, 239]), 229)

if __name__ == '__main__':
    unittest.main()