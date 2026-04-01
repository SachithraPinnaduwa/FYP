import unittest

class TestTariffCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = TariffCalculator(0.15, 1.5)

    def test_zero_consumption(self):
        self.assertEqual(self.calc.calculate_cost(0, 12, False), 0.0)
        self.assertEqual(self.calc.calculate_cost(0, 12, True), 0.0)

    def test_weekend_discount(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, True), 1.35)
        self.assertEqual(self.calc.calculate_cost(10, 12, False), 1.5)

    def test_peak_hours_multiplier(self):
        self.assertEqual(self.calc.calculate_cost(10, 18, False), 2.25)
        self.assertEqual(self.calc.calculate_cost(10, 18, True), 1.35)

    def test_non_peak_hours(self):
        self.assertEqual(self.calc.calculate_cost(10, 14, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 14, True), 1.35)

    def test_tax_included(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, False), 1.575)
        self.assertEqual(self.calc.calculate_cost(10, 18, False), 2.25)

    def test_negative_consumption(self):
        self.assertEqual(self.calc.calculate_cost(-5, 12, False), 0.0)
        self.assertEqual(self.calc.calculate_cost(-5, 12, True), 0.0)

    def test_large_consumption(self):
        self.assertEqual(self.calc.calculate_cost(1000, 12, False), 1575.0)
        self.assertEqual(self.calc.calculate_cost(1000, 18, False), 2250.0)

    def test_boundary_hours(self):
        self.assertEqual(self.calc.calculate_cost(10, 17, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 20, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 21, False), 1.5)

    def test_weekend_discount_applied(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, True), 1.35)
        self.assertEqual(self.calc.calculate_cost(10, 14, True), 1.35)

    def test_peak_hours_override_weekend_discount(self):
        self.assertEqual(self.calc.calculate_cost(10, 18, True), 1.35)
        self.assertEqual(self.calc.calculate_cost(10, 18, False), 2.25)

    def test_base_rate_zero(self):
        self.calc_zero = TariffCalculator(0.0, 1.5)
        self.assertEqual(self.calc_zero.calculate_cost(10, 12, False), 0.0)
        self.assertEqual(self.calc_zero.calculate_cost(10, 18, False), 0.0)

    def test_peak_multiplier_zero(self):
        self.calc_zero = TariffCalculator(0.15, 0.0)
        self.assertEqual(self.calc_zero.calculate_cost(10, 18, False), 0.0)
        self.assertEqual(self.calc_zero.calculate_cost(10, 12, False), 1.5)

    def test_consumption_is_float(self):
        self.assertEqual(self.calc.calculate_cost(10.5, 12, False), 1.605)
        self.assertEqual(self.calc.calculate_cost(10.5, 18, False), 1.575)

    def test_hour_of_day_is_int(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 18, False), 2.25)

    def test_is_weekend_is_bool(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 12, True), 1.35)

    def test_multiple_consumption_values(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 14, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 18, False), 2.25)

    def test_multiple_hour_of_day_values(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 14, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 18, False), 2.25)

    def test_multiple_is_weekend_values(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 12, True), 1.35)
        self.assertEqual(self.calc.calculate_cost(10, 18, True), 1.35)

    def test_multiple_combinations(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 12, True), 1.35)
        self.assertEqual(self.calc.calculate_cost(10, 14, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 14, True), 1.35)
        self.assertEqual(self.calc.calculate_cost(10, 18, False), 2.25)
        self.assertEqual(self.calc.calculate_cost(10, 18, True), 1.35)

    def test_multiple_combinations_with_different_consumption_values(self):
        self.assertEqual(self.calc.calculate_cost(10, 12, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 12, True), 1.35)
        self.assertEqual(self.calc.calculate_cost(10, 14, False), 1.5)
        self.assertEqual(self.calc.calculate_cost(10, 14, True), 1.35)
        self.assertEqual(self.calc.calculate_cost(10, 18, False), 2.25)
        self.assertEqual(self.calc.calculate_cost(10, 18, True), 1.35)
        self.assertEqual(self.calc.calculate_cost(20, 12, False), 3.0)
        self