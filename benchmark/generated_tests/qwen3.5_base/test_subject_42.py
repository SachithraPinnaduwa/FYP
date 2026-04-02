import unittest

class TestFuelCostCalculator(unittest.TestCase):
    def test_calculate_fuel_cost(self):
        # Test case 1: No discount
        self.assertEqual(calculate_fuel_cost(5, 1.5), 7.5)
        
        # Test case 2: Discount applied
        self.assertEqual(calculate_fuel_cost(15, 1.5), 18.75)
        
        # Test case 3: Maximum discount applied
        self.assertEqual(calculate_fuel_cost(100, 1.5), 112.5)
        
        # Test case 4: Zero litres
        self.assertEqual(calculate_fuel_cost(0, 1.5), 0.0)
        
        # Test case 5: Zero price per litre
        self.assertEqual(calculate_fuel_cost(10, 0), 0.0)
        
        # Test case 6: Negative litres (should not be allowed)
        with self.assertRaises(ValueError):
            calculate_fuel_cost(-5, 1.5)
        
        # Test case 7: Negative price per litre (should not be allowed)
        with self.assertRaises(ValueError):
            calculate_fuel_cost(10, -1.5)
        
        # Test case 8: Large number of litres
        self.assertEqual(calculate_fuel_cost(1000, 1.5), 1125.0)
        
        # Test case 9: Large price per litre
        self.assertEqual(calculate_fuel_cost(10, 100), 9975.0)
        
        # Test case 10: Very small price per litre
        self.assertEqual(calculate_fuel_cost(10, 0.01), 0.1)

if __name__ == '__main__':
    unittest.main()
