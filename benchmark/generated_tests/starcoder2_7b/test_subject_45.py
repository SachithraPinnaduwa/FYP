import unittest

class TestRepeater(unittest.TestCase):
    def test_repeater(self):
        self.assertEqual(repeater('yo', 3), '"yo" repeated 3 times is: "yoyoyo"')
        self.assertEqual(repeater('WuB', 6), '"WuB" repeated 6 times is: "WuBWuBWuBWuBWuBWuB"')

if __name__ == '__main__':
    unittest.main()

>>> repeater('yo', 3)
'"yo" repeated 3 times is: "yoyoyo"'
>>> repeater('WuB', 6)
'"WuB" repeated 6 times is: "WuBWuBWuBWuBWuBWuB"'