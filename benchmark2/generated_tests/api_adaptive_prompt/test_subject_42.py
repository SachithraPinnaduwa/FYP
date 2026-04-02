from subject_42 import *

import unittest

def calculate_fuel_cost(litres, price_per_litre):
    # Calculate the discount based on the number of litres
    discount_per_litre = int(min(litres, 10) / 2) * 0.05
    
    # Ensure the discount does not exceed the maximum allowed
    discount_per_litre = min(discount_per_litre, 0.25)
    
    # Calculate the final price per litre after discount
    final_price_per_litre = price_per_litre - discount_per_litre
    
    # Calculate the total cost
    total_cost = final_price_per_litre * litres
    
    # Return the total cost rounded to 2 decimal places
    return round(total_cost, 2)

class TestCalculateFuelCost(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(calculate_fuel_cost(3, 1.00), 2.85)

    def test_normal_case_2(self):
        self.assertEqual(calculate_fuel_cost(1, 1.00), 1.00)

    def test_normal_case_3(self):
        self.assertEqual(calculate_fuel_cost(10, 1.00), 9.00)

    def test_normal_case_4(self):
        self.assertEqual(calculate_fuel_cost(15, 1.00), 13.50)

    def test_edge_case_1(self):
        self.assertEqual(calculate_fuel_cost(0, 1.00), 0.00)

    def test_error_handling_1(self):
        with self.assertRaises(TypeError):
            calculate_fuel_cost('a', 1.00)

    def test_error_handling_2(self):
        with self.assertRaises(TypeError):
            calculate_fuel_cost(3, 'b')

    def test_edge_case_2(self):
        self.assertEqual(calculate_fuel_cost(100, 1.00), 95.00)

if __name__ == '__main__':
    unittest.main()