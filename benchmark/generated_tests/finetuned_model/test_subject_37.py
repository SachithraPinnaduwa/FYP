import unittest

class TestSecondSmallestOddPrimeGreaterThan100(unittest.TestCase):
    def test_with_multiple_primes(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 103, 107, 109, 113, 127, 131]), 103)
    
    def test_with_single_prime(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101]), 101)
    
    def test_with_all_same_prime(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 101, 101]), 101)
    
    def test_with_no_primes(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([102, 104, 106, 108]), float('inf'))
    
    def test_with_mixed_numbers(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([102, 104, 105, 106, 107, 108]), 107)
    
    def test_with_larger_numbers(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([102, 104, 105, 106, 107, 108, 109, 111, 113, 114]), 109)
    
    def test_with_single_element(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101]), 101)
    
    def test_with_negative_numbers(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([-101, -103, 101, 103]), 101)
    
    def test_with_float_values(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 103.5, 103, 105]), 103)

if __name__ == '__main__':
    unittest.main()