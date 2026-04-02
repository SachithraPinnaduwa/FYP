from subject_89 import *

import unittest

class TestQuantumTeleportation(unittest.TestCase):
    def test_quantum_teleportation(self):
        self.assertEqual(quantum_teleportation('hello', 'world'), 'hfnos')
        self.assertEqual(quantum_teleportation('test', 'key'), 't^t^')
        self.assertEqual(quantum_teleportation('1234', 'abcd'), '1^3^')
        self.assertEqual(quantum_teleportation('abc', 'xyz'), 'x^z^')

if __name__ == '__main__':
    unittest.main()