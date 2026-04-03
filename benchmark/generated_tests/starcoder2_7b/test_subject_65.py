```python
import unittest

class TestProcessIP(unittest.TestCase):
    def test_valid_ip(self):
        self.assertEqual(process_ip('192.168.0.1'), '192.168.0.1')
        self.assertEqual(process_ip('192.168.0.100'), '192.168.0.100')
        self.assertEqual(process_ip('192.168.0.255'), '192.168.0.255')

    def test_invalid_ip(self):
        self.assertEqual(process_ip('192.168.0'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.1.1'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.1000'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.256'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.001'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.010'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.1000'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.0001'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.00001'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.000001'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168.0.0000001'), 'IP address isn\'t valid')
        self.assertEqual(process_ip('192.168