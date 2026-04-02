import unittest

class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_small_numbers(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_large_numbers(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)
        self.assertEqual(fibonacci(40), 102334155)

    def test_edge_cases(self):
        self.assertEqual(fibonacci(1000), 43466557616402103962420423048458035117694656768161277151211682902577133687555886073388654802242574368971756465621304863560157769096779900318867508865198723168781751401206930217554975381511652809917361984791853121397312415196729970699)

if __name__ == '__main__':
    unittest.main()