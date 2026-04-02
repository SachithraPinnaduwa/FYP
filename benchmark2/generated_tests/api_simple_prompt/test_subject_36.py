from subject_36 import *

import unittest

def findCommonElements(array1, array2):
    commonElements = []
    dictionary = {}
    
    for element in array1:
        dictionary[element] = False
    
    for element in array2:
        if element in dictionary and not dictionary[element]:
            dictionary[element] = True
            commonElements.append(element)
    
    return commonElements

class TestFindCommonElements(unittest.TestCase):
    def test_findCommonElements(self):
        self.assertEqual(findCommonElements([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
        self.assertEqual(findCommonElements(['apple', 'banana', 'cherry'], ['banana', 'cherry', 'date']), ['banana', 'cherry'])
        self.assertEqual(findCommonElements([10, 20, 30], [40, 50, 60]), [])
        self.assertEqual(findCommonElements([], [1, 2, 3]), [])
        self.assertEqual(findCommonElements([1, 2, 3], []), [])
        self.assertEqual(findCommonElements([1, 2, 2, 3], [2, 2, 3, 4]), [2, 3])

if __name__ == '__main__':
    unittest.main()