from subject_50 import *

import unittest

def find_drag_race_winner(n, matches):
    # Dictionary to keep track of the winners and losers
    status = {}
    
    # Process each match result
    for match in matches:
        racer1, racer2 = match.split()
        
        # Initialize the status of racers if not already present
        if racer1 not in status:
            status[racer1] = True
        if racer2 not in status:
            status[racer2] = False
        
        # Update the status based on the match result
        if status[racer1]:
            status[racer2] = False
        else:
            status[racer1] = False
            status[racer2] = False
    
    # Find and return the winner
    for racer, is_winner in status.items():
        if is_winner:
            return racer

    # In case no winner is found (which shouldn't happen given the problem constraints)
    return None

class TestFindDragRaceWinner(unittest.TestCase):
    def test_normal_case_1(self):
        n = 2
        matches = ['a b', 'a c', 'c d']
        expected = 'a'
        self.assertEqual(find_drag_race_winner(n, matches), expected)

    def test_normal_case_2(self):
        n = 3
        matches = ['a b', 'a c', 'a d', 'b c', 'b d', 'c d', 'b a']
        expected = 'a'
        self.assertEqual(find_drag_race_winner(n, matches), expected)

    def test_edge_case_1(self):
        n = 1
        matches = ['a b']
        expected = 'a'
        self.assertEqual(find_drag_race_winner(n, matches), expected)

    def test_edge_case_2(self):
        n = 0
        matches = []
        expected = None
        self.assertEqual(find_drag_race_winner(n, matches), expected)

    def test_error_handling_1(self):
        n = -1
        matches = ['a b']
        with self.assertRaises(ValueError):
            find_drag_race_winner(n, matches)

    def test_error_handling_2(self):
        n = 2
        matches = ['a b', 'a c', 'c d', 'e f']
        with self.assertRaises(ValueError):
            find_drag_race_winner(n, matches)

if __name__ == '__main__':
    unittest.main()