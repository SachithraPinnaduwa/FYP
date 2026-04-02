import unittest

class TestSeparateDataTypes(unittest.TestCase):
    def test_separate_data_types(self):
        self.assertEqual(separate_data_types("10 20 30"), ([10, 20, 30], [], []))
        self.assertEqual(separate_data_types("10.5 20.5 30.5"), ([], [10.5, 20.5, 30.5], []))
        self.assertEqual(separate_data_types("10 20 abc"), ([10, 20], [], ['abc']))
        self.assertEqual(separate_data_types("abc def 123.45"), ([], [], ['abc', 'def', 123.45]))
        self.assertEqual(separate_data_types("10 abc 20.5 def"), ([10], [20.5], ['abc', 'def']))
        self.assertEqual(separate_data_types("abc def"), ([], [], ['abc', 'def']))
        self.assertEqual(separate_data_types(""), ([], [], []))
        self.assertEqual(separate_data_types("100.0001 200.0002"), ([], [100.0001, 200.0002], []))
        self.assertEqual(separate_data_types("100.0001 abc 200.0002"), ([100], [200.0002], ['abc']))
        self.assertEqual(separate_data_types("abc 100.0001 def 200.0002"), ([], [100.0001, 200.0002], ['abc', 'def']))
        self.assertEqual(separate_data_types("100.0001 abc 200.0002 def"), ([100], [200.0002], ['abc', 'def']))
        self.assertEqual(separate_data_types("abc 100.0001 def 200.0002"), ([], [100.0001, 200.0002], ['abc', 'def']))

if __name__ == '__main__':
    unittest.main()