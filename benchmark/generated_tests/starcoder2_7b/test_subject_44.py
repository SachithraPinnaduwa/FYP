import unittest

class Test(unittest.TestCase):
    def test_find_k_for_digit_power_sum(self):
        self.assertEqual(find_k_for_digit_power_sum(89, 1), 1)
        self.assertEqual(find_k_for_digit_power_sum(92, 1), -1)
        self.assertEqual(find_k_for_digit_power_sum(695, 2), 2)
        self.assertEqual(find_k_for_digit_power_sum(46288, 3), 51)

if __name__ == '__main__':
    unittest.main()

reverse('Hello World') should return 'dlroW olleH'
reverse('Kata') should return 'ataK'
reverse('123456789') should return '987654321'