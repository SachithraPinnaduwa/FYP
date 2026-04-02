import unittest

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(3, 4), 6)
        self.assertEqual(triangle_area(5, 12), 30)
        self.assertEqual(triangle_area(10, 24), 120)

if __name__ == '__main__':
    unittest.main()