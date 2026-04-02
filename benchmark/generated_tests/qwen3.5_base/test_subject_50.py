import unittest

class TestFindDragRaceWinner(unittest.TestCase):
    def test_case_1(self):
        # Test case 1: Basic scenario
        n = 3
        matches = ["A B", "B C", "A C"]
        self.assertEqual(find_drag_race_winner(n, matches), "A")
    
    def test_case_2(self):
        # Test case 2: Multiple winners
        n = 4
        matches = ["A B", "B C", "C D", "D A"]
        self.assertEqual(find_drag_race_winner(n, matches), "A")
    
    def test_case_3(self):
        # Test case 3: No winner
        n = 3
        matches = ["A B", "B C", "C A"]
        self.assertEqual(find_drag_race_winner(n, matches), None)
    
    def test_case_4(self):
        # Test case 4: Single match
        n = 2
        matches = ["A B"]
        self.assertEqual(find_drag_race_winner(n, matches), "A")
    
    def test_case_5(self):
        # Test case 5: Complex scenario
        n = 5
        matches = ["A B", "B C", "C D", "D E", "E A", "A C", "B D", "C E", "D A", "E B"]
        self.assertEqual(find_drag_race_winner(n, matches), "A")

if __name__ == '__main__':
    unittest.main()
