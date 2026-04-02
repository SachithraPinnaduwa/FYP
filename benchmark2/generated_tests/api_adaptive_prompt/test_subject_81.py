from subject_81 import *

import unittest

def find_min_number(N: str, d: str) -> str:
    a = list(N)
    w = int(d)
    count = 1
    l = []
    
    while True:
        if count != len(a):
            count = 1
            for i in range(len(a) - 1):
                if int(a[i]) > int(a[i + 1]):
                    a.pop(i)
                    a.append(d)
                    break
                else:
                    count += 1
        else:
            for i in range(len(a)):
                if int(a[i]) >= w:
                    l.append(a[i])
                    a.append(d)
                elif int(a[i]) == w:
                    break
            break
    
    for i in l:
        a.remove(i)
    
    return ''.join(a)

class TestFindMinNumber(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(find_min_number('35', '4'), '34')

    def test_normal_case_2(self):
        self.assertEqual(find_min_number('42', '4'), '24')

    def test_normal_case_3(self):
        self.assertEqual(find_min_number('24', '9'), '24')

    def test_edge_case_1(self):
        self.assertEqual(find_min_number('1', '2'), '12')

    def test_edge_case_2(self):
        self.assertEqual(find_min_number('999999999999999999', '1'), '1999999999999999999')

    def test_error_handling_1(self):
        with self.assertRaises(ValueError):
            find_min_number('', '1')

    def test_error_handling_2(self):
        with self.assertRaises(ValueError):
            find_min_number('abc', '1')

    def test_error_handling_3(self):
        with self.assertRaises(ValueError):
            find_min_number('123', 'a')

if __name__ == '__main__':
    unittest.main()