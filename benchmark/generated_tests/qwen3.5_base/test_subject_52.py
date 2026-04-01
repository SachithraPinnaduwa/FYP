import unittest

class TestSimpleRegexMatcher(unittest.TestCase):
    def setUp(self):
        self.matcher = SimpleRegexMatcher()
    
    def test_empty_pattern(self):
        self.assertTrue(self.matcher.match("", ""))
        self.assertFalse(self.matcher.match("", "a"))
        self.assertFalse(self.matcher.match("a", ""))
    
    def test_exact_match(self):
        self.assertTrue(self.matcher.match("abc", "abc"))
        self.assertFalse(self.matcher.match("abc", "ab"))
        self.assertFalse(self.matcher.match("abc", "abcd"))
    
    def test_wildcard_match(self):
        self.assertTrue(self.matcher.match("a.c", "abc"))
        self.assertTrue(self.matcher.match("a.c", "axc"))
        self.assertTrue(self.matcher.match("a.c", "a.c"))
        self.assertFalse(self.matcher.match("a.c", "ac"))
        self.assertFalse(self.matcher.match("a.c", "axc"))
    
    def test_star_match(self):
        self.assertTrue(self.matcher.match("a*", "a"))
        self.assertTrue(self.matcher.match("a*", "aa"))
        self.assertTrue(self.matcher.match("a*", "aaa"))
        self.assertTrue(self.matcher.match("a*", ""))
        self.assertFalse(self.matcher.match("a*", "b"))
        self.assertFalse(self.matcher.match("a*", "ab"))
    
    def test_combined_patterns(self):
        self.assertTrue(self.matcher.match("a*b*c", "ab"))
        self.assertTrue(self.matcher.match("a*b*c", "abc"))
        self.assertTrue(self.matcher.match("a*b*c", "axyc"))
        self.assertFalse(self.matcher.match("a*b*c", "ax"))
        self.assertFalse(self.matcher.match("a*b*c", "x"))
    
    def test_multiple_wildcards(self):
        self.assertTrue(self.matcher.match(".*", "abc"))
        self.assertTrue(self.matcher.match(".*", "a"))
        self.assertTrue(self.matcher.match(".*", ""))
        self.assertFalse(self.matcher.match(".*", "a.b"))
    
    def test_complex_pattern(self):
        self.assertTrue(self.matcher.match("a*b*c*d*", "ab"))
        self.assertTrue(self.matcher.match("a*b*c*d*", "abc"))
        self.assertTrue(self.matcher.match("a*b*c*d*", "axyc"))
        self.assertFalse(self.matcher.match("a*b*c*d*", "ax"))
        self.assertFalse(self.matcher.match("a*b*c*d*", "x"))
    
    def test_case_sensitivity(self):
        self.assertFalse(self.matcher.match("abc", "ABC"))
        self.assertFalse(self.matcher.match("ABC", "abc"))
    
    def test_empty_text(self):
        self.assertTrue(self.matcher.match(".*", ""))
        self.assertFalse(self.matcher.match("a", ""))
    
    def test_empty_pattern(self):
        self.assertTrue(self.matcher.match("", ""))
        self.assertFalse(self.matcher.match("", "a"))
        self.assertFalse(self.matcher.match("a", ""))
    
    def test_multiple_wildcards(self):
        self.assertTrue(self.matcher.match(".*", "abc"))
        self.assertTrue(self.matcher.match(".*", "a"))
        self.assertTrue(self.matcher.match(".*", ""))
        self.assertFalse(self.matcher.match(".*", "a.b"))
    
    def test_complex_pattern(self):
        self.assertTrue(self.matcher.match("a*b*c*d*", "ab"))
        self.assertTrue(self.matcher.match("a*b*c*d*", "abc"))
        self.assertTrue(self.matcher.match("a*b*c*d*", "axyc"))
        self.assertFalse(self.matcher.match("a*b*c*d*", "ax"))
        self.assertFalse(self.matcher.match("a*b*c*d*", "x"))
    
    def test_case_sensitivity(self):
        self.assertFalse(self.matcher.match("abc", "ABC"))
        self.assertFalse(self.matcher.match("ABC", "abc"))
    
    def test_empty_text(self):
        self.assertTrue(self.matcher.match(".*", ""))
        self.assertFalse(self.matcher.match("a", ""))
    
    def test_empty_pattern(self):
        self.assertTrue(self.matcher.match("", ""))
        self.assertFalse(self.matcher.match("", "a"))
        self.assertFalse(self.matcher.match("a", ""))
    
    def test_multiple_wildcards(self):
        self.assertTrue(self.matcher.match(".*", "abc"))
        self.assertTrue(self.matcher.match(".*", "a"))
        self.assertTrue(self.matcher.match(".*", ""))
        self.assertFalse(self.matcher.match(".*", "a.b"))
    
    def test_complex_pattern(self):
        self.assertTrue(self.matcher.match("a*b*c*d*", "ab"))
        self.assertTrue(self.matcher.match("a*b*c*d*", "abc"))
        self.assertTrue(self.matcher.match("a*b*c*d*", "axyc"))
        self.assertFalse(self.matcher.match("a*b*c*d*", "ax"))
        self.assertFalse(self.matcher.match("a*b*c*d*", "x"))
    
    def test_case_sensitivity(self):
        self.assertFalse(self.matcher.match("abc", "ABC"))
        self.assertFalse(self.matcher.match("ABC", "abc"))
    
    def test_empty_text(self):
        self.assertTrue(self.matcher.match(".*", ""))
        self.assertFalse(self.matcher.match("a", ""))
    
    def test_empty_pattern(self):
        self.assertTrue(self.matcher.match("", ""))
        self.assertFalse(self.matcher.match("", "a"))
        self.assertFalse(self.matcher.match("a", ""))
    
    def test_multiple_wildcards(self):
        self.assertTrue(self.matcher.match(".*", "abc"))
        self.assertTrue(self.matcher.match(".*", "a"))
        self.assertTrue(self.matcher.match(".*", ""))
        self.assertFalse(self.matcher.match(".*", "a.b"))
    
    def test_complex_pattern(self):
        self.assertTrue(self.matcher.match("a*b*c*d*", "ab"))
        self.assertTrue(self.matcher.match("a*b*c*d*", "abc"))
        self.assertTrue(self.matcher.match("a*b*c*d*", "axyc"))
        self.assertFalse(self.matcher.match("a*b*c*d*", "ax"))
        self.assertFalse(self.matcher.match("a*b*c*d*", "x"))
    
    def test_case_sensitivity(self):
        self.assertFalse(self.matcher.match("abc", "ABC"))
        self.assertFalse(self.matcher.match("ABC", "abc"))
    
    def test_empty_text(self):
        self.assertTrue(self.matcher.match(".*", ""))
        self.assertFalse(self.matcher.match("a", ""))
    
    def test_empty_pattern(self):
        self.assertTrue(self.matcher.match("", ""))
        self.assertFalse(self.matcher.match("", "a"))
        self.assertFalse(self.matcher.match("a", ""))
    
    def test_multiple_wildcards(self):
        self.assertTrue(self.matcher.match(".*", "abc"))
        self.assertTrue(self.matcher.match(".*", "a"))
        self.assertTrue(self.matcher.match(".*", ""))
        self.assertFalse(self.matcher.match(".*", "a.b"))
    
    def test_complex_pattern(self):
        self.assertTrue(self.matcher.match("a*b*c*d*", "ab"))
        self.assertTrue(self.matcher.match("a*b*c*d*", "abc"))
        self.assertTrue(self.matcher.match("