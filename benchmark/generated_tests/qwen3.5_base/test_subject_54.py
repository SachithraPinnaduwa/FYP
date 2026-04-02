import unittest

class TestContainsThreeOddPrimes(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19]))
    
    def test_case_2(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21]))
    
    def test_case_3(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23]))
    
    def test_case_4(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25]))
    
    def test_case_5(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27]))
    
    def test_case_6(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29]))
    
    def test_case_7(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31]))
    
    def test_case_8(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33]))
    
    def test_case_9(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]))
    
    def test_case_10(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]))
    
    def test_case_11(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]))
    
    def test_case_12(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]))
    
    def test_case_13(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]))
    
    def test_case_14(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]))
    
    def test_case_15(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]))
    
    def test_case_16(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]))
    
    def test_case_17(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]))
    
    def test_case_18(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53]))
    
    def test_case_19(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 4