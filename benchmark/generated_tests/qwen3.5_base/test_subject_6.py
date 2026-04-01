import unittest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("John Doe", 100.0)

    def test_initialization(self):
        self.assertEqual(self.account.owner, "John Doe")
        self.assertEqual(self.account.balance, 100.0)
        self.assertEqual(len(self.account.history), 0)

    def test_deposit(self):
        self.account.deposit(50.0)
        self.assertEqual(self.account.balance, 150.0)
        self.assertEqual(len(self.account.history), 1)
        self.assertEqual(self.account.history[0][0], "DEP")
        self.assertEqual(self.account.history[0][1], 50.0)
        self.assertIsInstance(self.account.history[0][2], datetime.datetime)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10.0)

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0.0)

    def test_deposit_multiple(self):
        self.account.deposit(20.0)
        self.account.deposit(30.0)
        self.assertEqual(self.account.balance, 150.0)
        self.assertEqual(len(self.account.history), 2)
        self.assertEqual(self.account.history[1][0], "DEP")
        self.assertEqual(self.account.history[1][1], 30.0)

if __name__ == '__main__':
    unittest.main()
