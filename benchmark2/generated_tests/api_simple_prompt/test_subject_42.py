from subject_42 import *

import unittest

class TestCalculateFuelCost(unittest.TestCase):
    def test_calculate_fuel_cost(self):
        self.assertEqual(calculate_fuel_cost(10, 3.50), 29.00)
        self.assertEqual(calculate_fuel_cost(5, 2.00), 9.50)
        self.assertEqual(calculate_fuel_cost(15, 1.50), 20.25)
        self.assertEqual(calculate_fuel_cost(2, 5.00), 9.50)
        self.assertEqual(calculate_fuel_cost(0, 10.00), 0.00)
        self.assertEqual(calculate_fuel_cost(1, 1.00), 1.00)

if __name__ == '__main__':
    unittest.main()