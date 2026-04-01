import unittest

class TestIPv4Network(unittest.TestCase):
    def test_init(self):
        network = IPv4Network("192.168.1.0/24")
        self.assertEqual(network.get_network_address(), "192.168.1.0")
        self.assertEqual(network.get_broadcast_address(), "192.168.1.255")

    def test_contains(self):
        network = IPv4Network("192.168.1.0/24")
        self.assertTrue(network.contains("192.168.1.100"))
        self.assertFalse(network.contains("192.168.2.1"))

    def test_ip_to_int(self):
        self.assertEqual(IPv4Network._ip_to_int("192.168.1.1"), 0xC0A80101)

    def test_int_to_ip(self):
        self.assertEqual(IPv4Network._int_to_ip(0xC0A80101), "192.168.1.1")

if __name__ == '__main__':
    unittest.main()
