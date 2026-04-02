import unittest

class TestFilterStrings(unittest.TestCase):
    def test_filter_strings(self):
        data = ['abc', 'def', 'ghi', 'jkl','mno', 'pqr','stu', 'vwx', 'yz']
        n = 3
        result = filter_strings(data, n)
        self.assertEqual(result, ['ghi', 'jkl','mno', 'pqr','stu', 'vwx', 'yz'])

if __name__ == '__main__':
    unittest.main()