# import unittest

# class TestSumListRecursive(unittest.TestCase):
#     def test_empty_list(self):
#         self.assertEqual(sum_list_recursive([]), 0)

#     def test_single_element_list(self):
#         self.assertEqual(sum_list_recursive([5]), 5)

#     def test_positive_numbers(self):
#         self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5]), 15)

#     def test_negative_numbers(self):
#         self.assertEqual(sum_list_recursive([-1, -2, -3, -4, -5]), -15)

#     def test_mixed_numbers(self):
#         self.assertEqual(sum_list_recursive([-1, 2, -3, 4, -5]), -5)

#     def test_large_numbers(self):
#         self.assertEqual(sum_list_recursive([1000000, 2000000, 3000000]), 6000000)

#     def test_single_large_number(self):
#         self.assertEqual(sum_list_recursive([1000000000000000000]), 1000000000000000000)

#     def test_single_small_number(self):
#         self.assertEqual(sum_list_recursive([1]), 1)

#     def test_large_number_of_small_numbers(self):
#         self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5] * 1000000), 5000000)

#     def test_large_number_of_large_numbers(self):
#         self.assertEqual(sum_list_recursive([1000000] * 1000000), 1000000000000)

#     def test_non_integer_elements(self):
#         with self.assertRaises(TypeError):
#             sum_list_recursive([1, '2', 3])

# if __name__ == '__main__':
#     unittest.main()