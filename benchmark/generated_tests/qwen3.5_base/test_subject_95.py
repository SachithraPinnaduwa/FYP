import unittest

class TestMinimumCostArborescence(unittest.TestCase):
    def test_single_node(self):
        self.assertEqual(minimum_cost_arborescence(1, 0, 0, []), 0)
    
    def test_two_nodes(self):
        self.assertEqual(minimum_cost_arborescence(2, 1, 0, [(0, 1, 10)]), 10)
    
    def test_three_nodes(self):
        self.assertEqual(minimum_cost_arborescence(3, 2, 0, [(0, 1, 10), (0, 2, 20)]), 30)
    
    def test_four_nodes(self):
        self.assertEqual(minimum_cost_arborescence(4, 3, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30)]), 60)
    
    def test_five_nodes(self):
        self.assertEqual(minimum_cost_arborescence(5, 4, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40)]), 100)
    
    def test_six_nodes(self):
        self.assertEqual(minimum_cost_arborescence(6, 5, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50)]), 150)
    
    def test_seven_nodes(self):
        self.assertEqual(minimum_cost_arborescence(7, 6, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50), (0, 6, 60)]), 210)
    
    def test_eight_nodes(self):
        self.assertEqual(minimum_cost_arborescence(8, 7, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50), (0, 6, 60), (0, 7, 70)]), 280)
    
    def test_nine_nodes(self):
        self.assertEqual(minimum_cost_arborescence(9, 8, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50), (0, 6, 60), (0, 7, 70), (0, 8, 80)]), 360)
    
    def test_ten_nodes(self):
        self.assertEqual(minimum_cost_arborescence(10, 9, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50), (0, 6, 60), (0, 7, 70), (0, 8, 80), (0, 9, 90)]), 450)
    
    def test_eleven_nodes(self):
        self.assertEqual(minimum_cost_arborescence(11, 10, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50), (0, 6, 60), (0, 7, 70), (0, 8, 80), (0, 9, 90), (0, 10, 100)]), 550)
    
    def test_twelve_nodes(self):
        self.assertEqual(minimum_cost_arborescence(12, 11, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50), (0, 6, 60), (0, 7, 70), (0, 8, 80), (0, 9, 90), (0, 10, 100), (0, 11, 110)]), 660)
    
    def test_thirteen_nodes(self):
        self.assertEqual(minimum_cost_arborescence(13, 12, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50), (0, 6, 60), (0, 7, 70), (0, 8, 80), (0, 9, 90), (0, 10, 100), (0, 11, 110), (0, 12, 120)]), 780)
    
    def test_fourteen_nodes(self):
        self.assertEqual(minimum_cost_arborescence(14, 13, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50), (0, 6, 60), (0, 7, 70), (0, 8, 80), (0, 9, 90), (0, 10, 100), (0, 11, 110), (0, 12, 120), (0, 13, 130)]), 910)
    
    def test_fifteen_nodes(self):
        self.assertEqual(minimum_cost_arborescence(15, 14, 0, [(0, 1, 10), (0, 2, 20), (0, 3, 30), (0, 4, 40), (0, 5, 50), (0, 6, 60),