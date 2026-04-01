import unittest

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()

    def test_add_stock(self):
        self.manager.add_stock("ITEM1", 10, 5.0)
        self.manager.add_stock("ITEM1", 5, 6.0)
        self.manager.add_stock("ITEM2", 3, 7.0)
        
        self.assertEqual(len(self.manager.stock), 2)
        self.assertEqual(self.manager.stock["ITEM1"][0]["qty"], 10)
        self.assertEqual(self.manager.stock["ITEM1"][1]["qty"], 5)
        self.assertEqual(self.manager.stock["ITEM2"][0]["qty"], 3)

    def test_sell_stock(self):
        self.manager.add_stock("ITEM1", 10, 5.0)
        self.manager.add_stock("ITEM1", 5, 6.0)
        
        cost = self.manager.sell_stock("ITEM1", 10)
        self.assertEqual(cost, 50.0)
        self.assertEqual(len(self.manager.stock["ITEM1"]), 1)
        self.assertEqual(self.manager.stock["ITEM1"][0]["qty"], 5)

    def test_sell_partial_stock(self):
        self.manager.add_stock("ITEM1", 10, 5.0)
        self.manager.add_stock("ITEM1", 5, 6.0)
        
        cost = self.manager.sell_stock("ITEM1", 7)
        self.assertEqual(cost, 35.0)
        self.assertEqual(self.manager.stock["ITEM1"][0]["qty"], 8)

    def test_sell_out_of_stock(self):
        self.manager.add_stock("ITEM1", 10, 5.0)
        self.manager.add_stock("ITEM1", 5, 6.0)
        
        with self.assertRaises(ValueError):
            self.manager.sell_stock("ITEM1", 20)

    def test_add_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.manager.add_stock("ITEM1", -5, 5.0)
        with self.assertRaises(ValueError):
            self.manager.add_stock("ITEM1", 0, 5.0)

    def test_sell_nonexistent_item(self):
        with self.assertRaises(ValueError):
            self.manager.sell_stock("ITEM99", 5)

    def test_transaction_log(self):
        self.manager.add_stock("ITEM1", 10, 5.0)
        self.manager.sell_stock("ITEM1", 10)
        
        self.assertEqual(len(self.manager.transactions), 1)
        self.assertEqual(self.manager.transactions[0]["item"], "ITEM1")
        self.assertEqual(self.manager.transactions[0]["sold"], 10)
        self.assertEqual(self.manager.transactions[0]["cogs"], 50.0)

if __name__ == "__main__":
    unittest.main()
