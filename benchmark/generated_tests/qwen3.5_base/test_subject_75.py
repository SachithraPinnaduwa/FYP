import unittest

class TestEloRatingSystem(unittest.TestCase):
    def setUp(self):
        self.system = EloRatingSystem()

    def test_add_player(self):
        self.system.add_player("PlayerA")
        self.assertEqual(self.system.ratings["PlayerA"], 1200.0)

    def test_add_player_with_custom_rating(self):
        self.system.add_player("PlayerB", 1500.0)
        self.assertEqual(self.system.ratings["PlayerB"], 1500.0)

    def test_get_expected_score(self):
        self.assertEqual(self.system.get_expected_score(1200.0, 1200.0), 0.5)
        self.assertLess(self.system.get_expected_score(1200.0, 1500.0), 0.5)
        self.assertGreater(self.system.get_expected_score(1500.0, 1200.0), 0.5)

    def test_record_match_win(self):
        self.system.add_player("PlayerA")
        self.system.add_player("PlayerB")
        self.system.record_match("PlayerA", "PlayerB", 1.0)
        self.assertGreater(self.system.ratings["PlayerA"], 1200.0)
        self.assertLess(self.system.ratings["PlayerB"], 1200.0)

    def test_record_match_draw(self):
        self.system.add_player("PlayerA")
        self.system.add_player("PlayerB")
        self.system.record_match("PlayerA", "PlayerB", 0.5)
        self.assertEqual(self.system.ratings["PlayerA"], self.system.ratings["PlayerB"])

    def test_record_match_loss(self):
        self.system.add_player("PlayerA")
        self.system.add_player("PlayerB")
        self.system.record_match("PlayerA", "PlayerB", 0.0)
        self.assertLess(self.system.ratings["PlayerA"], 1200.0)
        self.assertGreater(self.system.ratings["PlayerB"], 1200.0)

    def test_record_match_invalid_player(self):
        with self.assertRaises(ValueError):
            self.system.record_match("PlayerA", "PlayerC", 1.0)

    def test_custom_k_factor(self):
        custom_system = EloRatingSystem(k_factor=20.0)
        custom_system.add_player("PlayerA")
        custom_system.add_player("PlayerB")
        custom_system.record_match("PlayerA", "PlayerB", 1.0)
        self.assertEqual(custom_system.k_factor, 20.0)

if __name__ == "__main__":
    unittest.main()
