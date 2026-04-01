import unittest

class TestCalculateFuelCost(unittest.TestCase):

    # Test case with no discount
    def test_no_discount(self):
        litres = 1
        price_per_litre = 1.00
        expected_cost = 1.00
        self.assertEqual(calculate_fuel_cost(litres, price_per_litre), expected_cost)

    # Test case with a discount of 5 cents per litre
    def test_discount_5_cents(self):
        litres = 2
        price_per_litre = 1.00
        expected_cost = 1.90
        self.assertEqual(calculate_fuel_cost(litres, price_per_litre), expected_cost)

    # Test case with a discount of 10 cents per litre
    def test_discount_10_cents(self):
        litres = 4
        price_per_litre = 1.00
        expected_cost = 3.60
        self.assertEqual(calculate_fuel_cost(litres, price_per_litre), expected_cost)

    # Test case with a discount of 25 cents per litre
    def test_discount_25_cents(self):
        litres = 10
        price_per_litre = 1.00
        expected_cost = 9.00
        self.assertEqual(calculate_fuel_cost(litres, price_per_litre), expected_cost)

    # Test case with a maximum discount of 25 cents per litre
    def test_max_discount(self):
        litres = 15
        price_per_litre = 1.00
        expected_cost = 13.50
        self.assertEqual(calculate_fuel_cost(litres, price_per_litre), expected_cost)

    # Test case with a price per litre greater than 1.00
    def test_high_price_per_litre(self):
        litres = 5
        price_per_litre = 2.00
        expected_cost = 9.00
        self.assertEqual(calculate_fuel_cost(litres, price_per_litre), expected_cost)

    # Test case with a price per litre less than 1.00
    def test_low_price_per_litre(self):
        litres = 5
        price_per_litre = 0.50
        expected_cost = 2.00
        self.assertEqual(calculate_fuel_cost(litres, price_per_litre), expected_cost)