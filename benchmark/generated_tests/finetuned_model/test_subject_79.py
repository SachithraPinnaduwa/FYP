from unittest import TestCase, main

class TestReverseString(TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("ab"), "ba")
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("1234567890"), "0987654321")
        self.assertEqual(reverse_string("abcde"), "edcba")
        self.assertEqual(reverse_string("abcde"), "edcba")

if __name__ == '__main__':
    main()