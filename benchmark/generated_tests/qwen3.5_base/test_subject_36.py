import unittest

class TestFindCommonElements(unittest.TestCase):
    def test_empty_arrays(self):
        self.assertEqual(findCommonElements([], []), [])
    
    def test_no_common_elements(self):
        self.assertEqual(findCommonElements([1, 2, 3], [4, 5, 6]), [])
    
    def test_all_common_elements(self):
        self.assertEqual(findCommonElements([1, 2, 3], [1, 2, 3]), [1, 2, 3])
    
    def test_partial_common_elements(self):
        self.assertEqual(findCommonElements([1, 2, 3], [2, 3, 4]), [2, 3])
    
    def test_duplicate_elements(self):
        self.assertEqual(findCommonElements([1, 1, 2], [1, 2, 2]), [1, 2])
    
    def test_large_arrays(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1, 1001))
        self.assertEqual(findCommonElements(array1, array2), list(range(1, 1001)))
    
    def test_large_arrays_partial_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(500, 1500))
        self.assertEqual(findCommonElements(array1, array2), list(range(500, 1001)))
    
    def test_large_arrays_no_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1001, 2001))
        self.assertEqual(findCommonElements(array1, array2), [])
    
    def test_large_arrays_all_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1, 1001))
        self.assertEqual(findCommonElements(array1, array2), list(range(1, 1001)))
    
    def test_large_arrays_partial_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(500, 1500))
        self.assertEqual(findCommonElements(array1, array2), list(range(500, 1001)))
    
    def test_large_arrays_no_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1001, 2001))
        self.assertEqual(findCommonElements(array1, array2), [])
    
    def test_large_arrays_all_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1, 1001))
        self.assertEqual(findCommonElements(array1, array2), list(range(1, 1001)))
    
    def test_large_arrays_partial_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(500, 1500))
        self.assertEqual(findCommonElements(array1, array2), list(range(500, 1001)))
    
    def test_large_arrays_no_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1001, 2001))
        self.assertEqual(findCommonElements(array1, array2), [])
    
    def test_large_arrays_all_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1, 1001))
        self.assertEqual(findCommonElements(array1, array2), list(range(1, 1001)))
    
    def test_large_arrays_partial_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(500, 1500))
        self.assertEqual(findCommonElements(array1, array2), list(range(500, 1001)))
    
    def test_large_arrays_no_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1001, 2001))
        self.assertEqual(findCommonElements(array1, array2), [])
    
    def test_large_arrays_all_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1, 1001))
        self.assertEqual(findCommonElements(array1, array2), list(range(1, 1001)))
    
    def test_large_arrays_partial_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(500, 1500))
        self.assertEqual(findCommonElements(array1, array2), list(range(500, 1001)))
    
    def test_large_arrays_no_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1001, 2001))
        self.assertEqual(findCommonElements(array1, array2), [])
    
    def test_large_arrays_all_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1, 1001))
        self.assertEqual(findCommonElements(array1, array2), list(range(1, 1001)))
    
    def test_large_arrays_partial_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(500, 1500))
        self.assertEqual(findCommonElements(array1, array2), list(range(500, 1001)))
    
    def test_large_arrays_no_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1001, 2001))
        self.assertEqual(findCommonElements(array1, array2), [])
    
    def test_large_arrays_all_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(1, 1001))
        self.assertEqual(findCommonElements(array1, array2), list(range(1, 1001)))
    
    def test_large_arrays_partial_common(self):
        array1 = list(range(1, 1001))
        array2 = list(range(500, 1500))
        self.assertEqual(findCommonElements(array1, array2), list(range(500, 1001)))
    
    def test_large_arrays_no_common(self):
        array1 = list(range(1, 10