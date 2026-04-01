import unittest

class TestFindMinNumber(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(find_min_number("35", "4"), "34")

    def test_case_2(self):
        self.assertEqual(find_min_number("42", "4"), "24")

    def test_case_3(self):
        self.assertEqual(find_min_number("24", "9"), "24")

    def test_case_4(self):
        self.assertEqual(find_min_number("123456789", "1"), "1123456789")

    def test_case_5(self):
        self.assertEqual(find_min_number("987654321", "9"), "9987654321")

    def test_case_6(self):
        self.assertEqual(find_min_number("111111", "1"), "111111")

    def test_case_7(self):
        self.assertEqual(find_min_number("23456789", "0"), "23456789")

    def test_case_8(self):
        self.assertEqual(find_min_number("999999", "9"), "999999")

    def test_case_9(self):
        self.assertEqual(find_min_number("123456789", "2"), "1223456789")

    def test_case_10(self):
        self.assertEqual(find_min_number("987654321", "8"), "9887654321")

if __name__ == '__main__':
    unittest.main()