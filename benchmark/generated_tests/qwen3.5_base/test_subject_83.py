import unittest

class TestMakeStringsEqual(unittest.TestCase):
    def test_case_1(self):
        s = "ab"
        t = "ba"
        expected = (1, [(1, 2)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_2(self):
        s = "aa"
        t = "bb"
        expected = (-1, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_3(self):
        s = "ab"
        t = "ab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_4(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_5(self):
        s = "aaaa"
        t = "bbbb"
        expected = (-1, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_6(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_7(self):
        s = "ab"
        t = "ab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_8(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_9(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_10(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_11(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_12(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_13(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_14(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_15(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_16(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_17(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_18(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_19(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_20(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_21(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_22(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_23(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_24(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_25(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_26(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_27(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_28(self):
        s = "abab"
        t = "baba"
        expected = (2, [(1, 2), (3, 4)])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_29(self):
        s = "abab"
        t = "abab"
        expected = (0, [])
        self.assertEqual(make_strings_equal(s, t), expected)
    
    def test_case_30(self):
        s = "abab"