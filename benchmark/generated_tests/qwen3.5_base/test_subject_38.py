import unittest

class TestWeightedRoundRobin(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(WeightedRoundRobin({}).get_next(), None)
        
    def test_single(self):
        self.assertEqual(WeightedRoundRobin({"A": 1}).get_next(), "A")
        
    def test_two(self):
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 1}).get_next(), "A")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 1}).get_next(), "B")
        
    def test_three(self):
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 1, "C": 1}).get_next(), "A")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 1, "C": 1}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 1, "C": 1}).get_next(), "C")
        
    def test_weights(self):
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2}).get_next(), "A")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2}).get_next(), "A")
        
    def test_weights_three(self):
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3}).get_next(), "A")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3}).get_next(), "C")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3}).get_next(), "C")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3}).get_next(), "A")
        
    def test_weights_four(self):
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4}).get_next(), "A")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4}).get_next(), "C")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4}).get_next(), "D")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4}).get_next(), "D")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4}).get_next(), "C")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4}).get_next(), "A")
        
    def test_weights_five(self):
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "A")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "C")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "D")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "E")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "E")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "D")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "C")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}).get_next(), "A")
        
    def test_weights_six(self):
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}).get_next(), "A")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}).get_next(), "B")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}).get_next(), "C")
        self.assertEqual(WeightedRoundRobin({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "