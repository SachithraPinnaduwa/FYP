import unittest

class TestABTestAssigner(unittest.TestCase):
    def setUp(self):
        self.assigner = ABTestAssigner()
        
    def test_add_experiment(self):
        self.assigner.add_experiment("exp1", {"A": 50, "B": 50})
        self.assertIn("exp1", self.assigner.experiments)
        
    def test_add_experiment_invalid(self):
        with self.assertRaises(ValueError):
            self.assigner.add_experiment("exp2", {"A": 60, "B": 40})
            
    def test_get_variant(self):
        self.assigner.add_experiment("exp1", {"A": 50, "B": 50})
        self.assertEqual(self.assigner.get_variant("user1", "exp1"), "A")
        self.assertEqual(self.assigner.get_variant("user2", "exp1"), "B")
        
    def test_get_variant_control(self):
        self.assigner.add_experiment("exp1", {"A": 50, "B": 50})
        self.assertEqual(self.assigner.get_variant("user1", "nonexistent"), "Control")
        
    def test_get_variant_consistency(self):
        self.assigner.add_experiment("exp1", {"A": 50, "B": 50})
        self.assertEqual(self.assigner.get_variant("user1", "exp1"), self.assigner.get_variant("user1", "exp1"))
        
    def test_get_variant_distribution(self):
        self.assigner.add_experiment("exp1", {"A": 30, "B": 70})
        results = {}
        for i in range(1000):
            results[self.assigner.get_variant(f"user{i}", "exp1")] += 1
        self.assertIn("A", results)
        self.assertIn("B", results)
        self.assertLess(results["A"], 40)
        self.assertLess(results["B"], 80)

if __name__ == "__main__":
    unittest.main()
