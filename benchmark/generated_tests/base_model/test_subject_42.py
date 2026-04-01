import unittest

def calculate_fuel_cost(litres, price_per_litre):
    discount_per_litre = int(min(litres, 10) / 2) * 0.05
    discount_per_litre = min(discount_per_litre, 0.25)
    final_price_per_litre = price_per_litre - discount_per_litre
    total_cost = final_price_per_litre * litres
    return round(total_cost, 2)

class TestCalculateFuelCost(unittest.TestCase):

    def test_no_discount(self):
        self.assertEqual(calculate_fuel_cost(1, 1.00), 1.00)
        self.assertEqual(calculate_fuel_cost(3, 1.00), 3.00)
        self.assertEqual(calculate_fuel_cost(9, 1.00), 9.00)

    def test_two_litre_discount(self):
        self.assertEqual(calculate_fuel_cost(2, 1.00), 1.90)
        self.assertEqual(calculate_fuel_cost(4, 1.00), 3.60)
        self.assertEqual(calculate_fuel_cost(8, 1.00), 7.20)

    def test_four_litre_discount(self):
        self.assertEqual(calculate_fuel_cost(4, 1.00), 3.60)
        self.assertEqual(calculate_fuel_cost(6, 1.00), 5.40)
        self.assertEqual(calculate_fuel_cost(10, 1.00), 9.00)

    def test_ten_litre_discount(self):
        self.assertEqual(calculate_fuel_cost(10, 1.00), 9.00)
        self.assertEqual(calculate_fuel_cost(12, 1.00), 10.80)
        self.assertEqual(calculate_fuel_cost(20, 1.00), 18.00)

    def test_maximum_discount(self):
        self.assertEqual(calculate_fuel_cost(10, 1.00), 9.00)
        self.assertEqual(calculate_fuel_cost(12, 1.00), 10.80)
        self.assertEqual(calculate_fuel_cost(20, 1.00), 18.00)

    def test_higher_prices(self):
        self.assertEqual(calculate_fuel_cost(2, 2.00), 3.80)
        self.assertEqual(calculate_fuel_cost(4, 2.00), 6.40)
        self.assertEqual(calculate_fuel_cost(8, 2.00), 11.20)

if __name__ == '__main__':
    unittest.main()