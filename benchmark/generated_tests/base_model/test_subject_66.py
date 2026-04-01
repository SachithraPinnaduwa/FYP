import unittest

class TestGenerateMatrices(unittest.TestCase):

    def test_generate_matrices_with_single_matrix(self):
        result = generate_matrices(1)
        self.assertEqual(len(result), 1)
        self.assertIn(result[0], range(-400, 401))

    def test_generate_matrices_with_multiple_matrices(self):
        result = generate_matrices(5)
        self.assertEqual(len(result), 5)
        for diagonal_sum in result:
            self.assertIn(diagonal_sum, range(-400, 401))

    def test_generate_matrices_with_zero_matrices(self):
        with self.assertRaises(ValueError):
            generate_matrices(0)

    def test_generate_matrices_with_negative_number_of_matrices(self):
        with self.assertRaises(ValueError):
            generate_matrices(-1)

    def test_generate_matrices_with_large_number_of_matrices(self):
        import time
        start_time = time.time()
        generate_matrices(10**6)
        end_time = time.time()
        self.assertLessEqual(end_time - start_time, 10)  # Allow up to 10 seconds

if __name__ == '__main__':
    unittest.main()