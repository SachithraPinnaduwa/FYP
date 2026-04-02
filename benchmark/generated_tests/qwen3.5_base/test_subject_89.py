import unittest

class TestQuantumTeleportation(unittest.TestCase):
    def test_basic_teleportation(self):
        message = "Hello"
        key = "World"
        result = quantum_teleportation(message, key)
        self.assertEqual(result, "Hllo")

    def test_empty_message(self):
        message = ""
        key = "Key"
        result = quantum_teleportation(message, key)
        self.assertEqual(result, "")

    def test_long_message(self):
        message = "This is a long message"
        key = "This is a long key"
        result = quantum_teleportation(message, key)
        self.assertEqual(result, "XgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgXgX