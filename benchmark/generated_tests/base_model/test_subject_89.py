import unittest

class TestQuantumTeleportation(unittest.TestCase):

    def test_quantum_teleportation(self):
        self.assertEqual(quantum_teleportation('hello', 'world'), '\x16\x0f\x0e\x0d\x0c')
        self.assertEqual(quantum_teleportation('abc', 'xyz'), '\x97\x8a\x89')
        self.assertEqual(quantum_teleportation('test', ''), '')
        self.assertEqual(quantum_teleportation('', 'key'), '')

if __name__ == '__main__':
    unittest.main()