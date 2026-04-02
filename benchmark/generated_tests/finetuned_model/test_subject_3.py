import unittest

def factorial_(num):
    """Find the factorial of a given number"""
    # base case: factorial of 0 & 1 is 1
    if num == 0 or num == 1:
        return 1
    else:
        # recursive case: n! = n * (n-1)!
        return num * factorial_(num - 1)

class TestFactorial_(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(factorial_(0), 1)
        self.assertEqual(factorial_(1), 1)
    
    def test_positive_integers(self):
        self.assertEqual(factorial_(2), 2)
        self.assertEqual(factorial_(3), 6)
        self.assertEqual(factorial_(4), 24)
        self.assertEqual(factorial_(5), 120)
    
    def test_large_numbers(self):
        self.assertEqual(factorial_(10), 3628800)
        self.assertEqual(factorial_(15), 1307674368000)
    
    def test_high_precision_numbers(self):
        expected_100 = 933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000000
        self.assertEqual(factorial_(100), expected_100)
    
    def test_edge_cases(self):
        with self.assertRaises(RecursionError):
            factorial_(10000)

if __name__ == '__main__':
    unittest.main()