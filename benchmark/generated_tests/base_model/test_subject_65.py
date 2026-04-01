import unittest

class TestProcessIP(unittest.TestCase):

    def test_valid_ip(self):
        self.assertEqual(process_ip('192.168.1.1'), '19216811')

    def test_invalid_ip_too_many_parts(self):
        self.assertEqual(process_ip('192.168.1.1.1'), 'IP address isn''t valid')

    def test_invalid_ip_not_enough_parts(self):
        self.assertEqual(process_ip('192.168.1'), 'IP address isn''t valid')

    def test_invalid_ip_non_digit_part(self):
        self.assertEqual(process_ip('192.abc.1.1'), 'IP address isn''t valid')

    def test_invalid_ip_out_of_range(self):
        self.assertEqual(process_ip('192.256.1.1'), 'IP address isn''t valid')
        self.assertEqual(process_ip('-1.1.1.1'), 'IP address isn''t valid')

    def test_invalid_ip_leading_zero(self):
        self.assertEqual(process_ip('192.016.1.1'), 'IP address isn''t valid')
        self.assertEqual(process_ip('192.0.1.1'), '01611')

if __name__ == '__main__':
    unittest.main()