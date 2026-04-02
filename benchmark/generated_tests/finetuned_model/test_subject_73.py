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
    def test_single_prime(self):
        self.assertEqual(entrance(2, 2), [2])
    
    def test_multiple_primes(self):
        self.assertEqual(entrance(3, 11), [3, 5, 7, 11])
    
    def test_no_primes(self):
        self.assertEqual(entrance(4, 8), [5, 7])
    
    def test_single_number(self):
        self.assertEqual(entrance(10, 10), [])
    
    def test_start_greater_than_end(self):
        self.assertEqual(entrance(10, 1), [])
    
    def test_large_range(self):
        self.assertEqual(entrance(100, 110), [101, 103, 107, 109])
    
    def test_edge_case_start_zero(self):
        self.assertEqual(entrance(0, 2), [2])
    
    def test_edge_case_negative_number(self):
        self.assertEqual(entrance(-5, 2), [2])

if __name__ == '__main__':
    unittest.main()