import unittest

class Test(unittest.TestCase):
    def test_max_tower_height(self):
        self.assertEqual(max_tower_height(3, [(1, 5, 1), (2, 6, 2), (3, 7, 3)]), 6)
        self.assertEqual(max_tower_height(4, [(1, 2, 1), (1, 3, 3), (4, 6, 2), (5, 7, 1)]), 4)

if __name__ == '__main__':
    unittest.main()
/README.md
# Python-Unit-Testing

## Description

This repository contains a collection of Python unit tests for various coding problems.

## Usage

To use the unit tests, simply clone the repository and run the Python file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
/test_max_tower_height.py
import unittest

def max_tower_height(n, rings):
    aux = [(float('inf'), 0, 0)]  # Initialize with a sentinel value
    for a, b, h in rings:
        aux.append((b, a, h))
    aux.sort(reverse=True)
    
    s = [0]
    p = [0] * (n + 1)
    
    for i in range(1, n + 1):
        while aux[s[-1]][1] >= aux[i][0]:
            s.pop()
        p[i] = p[s[-1]] + aux[i][2]
        s.append(i)
    
    return max(p)

class Test(unittest.TestCase):
    def test_max_tower_height(self):
        self.assertEqual(max_tower_height(3, [(1, 5, 1), (2, 6, 2), (3, 7, 3)]), 6)
        self.assertEqual(max_tower_height(4, [(1, 2, 1), (1, 3, 3),