from subject_65 import *

import unittest

class TestProcessIP(unittest.TestCase):
    def test_valid_ip(self):
        self.assertEqual(process_ip('192.168.1.1'), '19216811')

    def test_invalid_ip_too_many_parts(self):
        self.assertEqual(process_ip('192.168.1.1.1'), 'IP address isn''t valid')

    def test_invalid_ip_too_few_parts(self):
        self.assertEqual(process_ip('192.168.1'), 'IP address isn''t valid')

    def test_invalid_ip_non_digit_part(self):
        self.assertEqual(process_ip('192.168.a.1'), 'IP address isn''t valid')

    def test_invalid_ip_out_of_range(self):
        self.assertEqual(process_ip('192.168.256.1'), 'IP address isn''t valid')

    def test_invalid_ip_leading_zero(self):
        self.assertEqual(process_ip('192.168.01.1'), 'IP address isn''t valid')

if __name__ == '__main__':
    unittest.main()