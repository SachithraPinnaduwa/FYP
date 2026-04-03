import unittest

class Test(unittest.TestCase):
    def test_calculate_robot_locations(self):
        self.assertEqual(calculate_robot_locations(1), 4)
        self.assertEqual(calculate_robot_locations(2), 4)
        self.assertEqual(calculate_robot_locations(3), 12)

if __name__ == '__main__':
    unittest.main()

### Explanation:

The robot can end up in any of the 4 corners of a square with side length $n$.

The robot can end up in any of the 4 corners of a square with side length $n - 1$.

The robot can end up in any of the 4 corners of a square with side length $n - 2$.

The robot can end up in any of the 4 corners of a square with side length $n - 3$.

The robot can end up in any of the 4 corners of a square with side length $n - 4$.

The robot can end up in any of the 4 corners of a square with side length $n - 5$.

The robot can end up in any of the 4 corners of a square with side length $n - 6$.

The robot can end up in any of the 4 corners of a square with side length $n - 7$.

The robot can end up in any of the 4 corners of a square with side length $n - 8$.

The robot can end up in any of the 4 corners of a square with side length $n - 9$.

The robot can end up in any of the 4 corners of a square with side length $n - 10$.

The robot can end up in any of the 4 corners of a square with side length $n - 11$.

The robot can end up in any of the 4 corners of a square with side length $n - 12$.

The robot can end up in any of the 4 corners of a square with side length $n - 13$.

The robot can end up in any of the 4 corners of a square with side length $n - 14$.

The robot can end up in any of the 4 corners of a square with side length $n - 15