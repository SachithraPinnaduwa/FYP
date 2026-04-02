import unittest

class TestDragRaceWinner(unittest.TestCase):
    def test_find_drag_race_winner(self):
        # Test case 1
        n1 = 2
        matches1 = ["a b", "a c", "c d"]
        expected1 = "a"
        self.assertEqual(find_drag_race_winner(n1, matches1), expected1)
        
        # Test case 2
        n2 = 1
        matches2 = ["x y"]
        expected2 = "x"
        self.assertEqual(find_drag_race_winner(n2, matches2), expected2)
        
        # Test case 3
        n3 = 3
        matches3 = ["p q", "r s", "p r", "p s"]
        expected3 = "p"
        self.assertEqual(find_drag_race_winner(n3, matches3), expected3)
        
        # Test case 4
        n4 = 2
        matches4 = ["u v", "u w", "u v"]
        expected4 = "u"
        self.assertEqual(find_drag_race_winner(n4, matches4), expected4)
        
        # Test case 5
        n5 = 3
        matches5 = ["m n", "o p", "q r", "m o", "n p", "m q"]
        expected5 = "m"
        self.assertEqual(find_drag_race_winner(n5, matches5), expected5)

if __name__ == '__main__':
    unittest.main()