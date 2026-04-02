import unittest

class TestEntrance(unittest.TestCase):
    def test_entrance(self):
        N = 4
        expected = [100, 200, 300, 400]
        result = entrance(N)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
