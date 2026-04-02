from subject_79 import *

import unittest

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("ab"), "ba")
        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("123456789"), "987654321")
        self.assertEqual(reverse_string("The quick brown fox jumps over the lazy dog"), "god yzal eht revo spmuj xof nworb kciuq ehT")
        self.assertEqual(reverse_string("A man, a plan, a canal, Panama"), "amanaP ,lanac a ,nalp a ,nam A")
        self.assertEqual(reverse_string("Madam, in Eden, I'm Adam"), "madA m'I ,nedE ni ,madaM")

if __name__ == '__main__':
    unittest.main()