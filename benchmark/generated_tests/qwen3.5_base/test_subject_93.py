import unittest

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = SimpleBlockchain()

    def test_create_genesis_block(self):
        genesis = self.blockchain.create_genesis_block()
        self.assertEqual(genesis.index, 0)
        self.assertEqual(genesis.data, "Genesis Block")
        self.assertEqual(genesis.previous_hash, "0")

    def test_add_block(self):
        self.blockchain.add_block("Test Data")
        latest = self.blockchain.get_latest_block()
        self.assertEqual(latest.index, 1)
        self.assertEqual(latest.data, "Test Data")
        self.assertEqual(latest.previous_hash, self.blockchain.chain[0].hash)

    def test_is_valid(self):
        self.assertTrue(self.blockchain.is_valid())
        self.blockchain.add_block("Test Data")
        self.assertTrue(self.blockchain.is_valid())

    def test_invalid_chain(self):
        self.blockchain.add_block("Test Data")
        self.blockchain.chain[1].previous_hash = "0"
        self.assertFalse(self.blockchain.is_valid())

if __name__ == '__main__':
    unittest.main()
