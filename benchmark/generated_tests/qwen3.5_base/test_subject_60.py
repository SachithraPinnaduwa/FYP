import unittest

class TestSubscriptionManager(unittest.TestCase):
    def setUp(self):
        self.manager = SubscriptionManager(monthly_rate=19.99)

    def test_subscribe_creates_trial(self):
        self.manager.subscribe("user1")
        self.assertEqual(self.manager.users["user1"]["status"], "TRIAL")
        self.assertEqual(self.manager.users["user1"]["balance"], 0.0)

    def test_charge_user_in_trial(self):
        self.manager.subscribe("user2")
        self.manager.charge_user("user2")
        self.assertEqual(self.manager.users["user2"]["status"], "ACTIVE")
        self.assertEqual(self.manager.users["user2"]["balance"], 19.99)

    def test_charge_user_outside_trial(self):
        self.manager.subscribe("user3")
        self.manager.charge_user("user3")
        self.manager.charge_user("user3")
        self.assertEqual(self.manager.users["user3"]["balance"], 39.98)

    def test_cancel_user(self):
        self.manager.subscribe("user4")
        self.manager.cancel("user4")
        self.assertEqual(self.manager.users["user4"]["status"], "CANCELLED")

    def test_charge_cancelled_user(self):
        self.manager.subscribe("user5")
        self.manager.cancel("user5")
        self.assertFalse(self.manager.charge_user("user5"))

if __name__ == "__main__":
    unittest.main()
