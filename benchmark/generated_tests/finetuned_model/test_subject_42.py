import unittest

def calculate_fuel_cost(litres, price_per_litre):
    discount_per_litre = int(min(litres, 10) / 2) * 0.05
    discount_per_litre = min(discount_per_litre, 0.25)
    final_price_per_litre = price_per_litre - discount_per_litre
    total_cost = final_price_per_litre * litres
    return round(total_cost, 2)

class TestCalculateFuelCost(unittest.TestCase):
    def test_calculate_fuel_cost(self):
        self.assertEqual(calculate_fuel_cost(10, 3.50), 29.00)
        self.assertEqual(calculate_fuel_cost(2, 3.50), 6.50)
        self.assertEqual(calculate_fuel_cost(4, 3.50), 13.00)
        self.assertEqual(calculate_fuel_cost(15, 3.50), 42.75)
        self.assertEqual(calculate_fuel_cost(0, 3.50), 0.00)
        self.assertEqual(calculate_fuel_cost(1, 3.50), 3.50)
        self.assertEqual(calculate_fuel_cost(100, 1.00), 75.00)

if __name__ == '__main__':
    unittest.main()