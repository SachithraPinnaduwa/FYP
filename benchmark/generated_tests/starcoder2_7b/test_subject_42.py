```if:python,php
import unittest

class TestDiscount(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(calculate_fuel_cost(1, 10), 10.00)
        self.assertEqual(calculate_fuel_cost(2, 10), 10.00)
        self.assertEqual(calculate_fuel_cost(3, 10), 10.50)
        self.assertEqual(calculate_fuel_cost(4, 10), 11.00)
        self.assertEqual(calculate_fuel_cost(5, 10), 11.50)
        self.assertEqual(calculate_fuel_cost(6, 10), 12.00)
        self.assertEqual(calculate_fuel_cost(7, 10), 12.50)
        self.assertEqual(calculate_fuel_cost(8, 10), 13.00)
        self.assertEqual(calculate_fuel_cost(9, 10), 13.50)
        self.assertEqual(calculate_fuel_cost(10, 10), 14.00)
        self.assertEqual(calculate_fuel_cost(11, 10), 14.50)
        self.assertEqual(calculate_fuel_cost(12, 10), 15.00)
        self.assertEqual(calculate_fuel_cost(13, 10), 15.50)
        self.assertEqual(calculate_fuel_cost(14, 10), 16.00)
        self.assertEqual(calculate_fuel_cost(15, 10), 16.50)
        self.assertEqual(calculate_fuel_cost(16, 10), 17.00)
        self.assertEqual(calculate_fuel_cost(17, 10), 17.50)
        self.assertEqual(calculate_fuel_cost(18, 10), 18.00)
        self.assertEqual(calculate_fuel_cost(19, 10), 18.50)
        self.assertEqual(calculate_fuel_cost(20, 10),