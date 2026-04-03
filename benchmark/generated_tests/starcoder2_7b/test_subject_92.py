import unittest

class TestFindMaxAdjacentFloors(unittest.TestCase):
    def test_find_max_adjacent_floors(self):
        self.assertEqual(find_max_adjacent_floors(15), (1, 5))
        self.assertEqual(find_max_adjacent_floors(16), (16, 1))
        self.assertEqual(find_max_adjacent_floors(2), (1, 1))
        self.assertEqual(find_max_adjacent_floors(3), (1, 2))
        self.assertEqual(find_max_adjacent_floors(9699690), (16, 4389))
        self.assertEqual(find_max_adjacent_floors(223092870), (129, 20995))
        self.assertEqual(find_max_adjacent_floors(847288609), (4112949, 206))
        self.assertEqual(find_max_adjacent_floors(900660121), (15006, 30011))
        self.assertEqual(find_max_adjacent_floors(987698769), (46887, 17718))
        self.assertEqual(find_max_adjacent_floors(999999999), (163837, 5994))

if __name__ == '__main__':
    unittest.main()
/README.md
# Python-Unit-Testing

## Description

This repository contains a collection of Python unit tests for various programming problems.

## Table of Contents

- [Python-Unit-Testing](#python-unit-testing)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Installation

To install the Python unit testing framework, you can use the following command:

```bash
pip install unittest
```

## Usage

To use the Python unit testing framework