import unittest

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string(''), '')
        self.assertEqual(reverse_string('abc'), 'cba')
        self.assertEqual(reverse_string('123'), '321')
        self.assertEqual(reverse_string('!@#$%^&*()'), '()*&^%$#@!')
        self.assertEqual(reverse_string('Hello, world!'), '!dlrow,olleH')
        self.assertEqual(reverse_string('你好，世界！'), '！世界，好你')

if __name__ == '__main__':
    unittest.main()