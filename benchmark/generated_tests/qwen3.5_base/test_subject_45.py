import unittest

class TestStandardDeviationCalc(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(StandardDeviationCalc([]).compute_std_dev(), 0.0)

    def test_single_element(self):
        self.assertEqual(StandardDeviationCalc([5]).compute_std_dev(), 0.0)

    def test_two_elements(self):
        self.assertEqual(StandardDeviationCalc([1, 3]).compute_std_dev(), 1.0)

    def test_large_dataset(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertAlmostEqual(StandardDeviationCalc(data).compute_std_dev(), 2.8722813233260237, places=10)

    def test_negative_numbers(self):
        data = [-1, -2, -3, -4, -5]
        self.assertAlmostEqual(StandardDeviationCalc(data).compute_std_dev(), 2.23606797749979, places=10)

    def test_float_values(self):
        data = [1.5, 2.5, 3.5, 4.5, 5.5]
        self.assertAlmostEqual(StandardDeviationCalc(data).compute_std_dev(), 1.5811388300841898, places=10)

    def test_mixed_types(self):
        data = [1, 2.5, 3, 4.5, 5]
        self.assertAlmostEqual(StandardDeviationCalc(data).compute_std_dev(), 1.5811388300841898, places=10)

    def test_large_variance(self):
        data = [1, 100, 200, 300, 400]
        self.assertAlmostEqual(StandardDeviationCalc(data).compute_std_dev(), 141.4213562373095, places=10)

    def test_zero_variance(self):
        data = [5, 5, 5, 5, 5]
        self.assertEqual(StandardDeviationCalc(data).compute_std_dev(), 0.0)

    def test_mean_calculation(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(StandardDeviationCalc(data).mean, 3.0)

    def test_variance_calculation(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(StandardDeviationCalc(data).compute_variance(), 2.0, places=10)

if __name__ == '__main__':
    unittest.main()
