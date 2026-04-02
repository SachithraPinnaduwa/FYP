from subject_65 import *

import unittest

def process_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return "IP address isn't valid"
    for part in parts:
        if not part.isdigit():
            return "IP address isn't valid"
        i = int(part)
        if i < 0 or i > 255:
            return "IP address isn't valid"
        if part[0] == '0' and len(part) != 1:
            return "IP address isn't valid"
    return ''.join(parts)

class TestProcessIP(unittest.TestCase):
    def test_valid_ip_no_leading_zeros(self):
        self.assertEqual(process_ip("192.168.1.1"), "19216811")

    def test_valid_ip_with_leading_zeros(self):
        self.assertEqual(process_ip("192.168.01.01"), "19216811")

    def test_valid_ip_all_single_digit(self):
        self.assertEqual(process_ip("1.1.1.1"), "1111")

    def test_valid_ip_all_zeros(self):
        self.assertEqual(process_ip("0.0.0.0"), "0000")

    def test_invalid_ip_empty_part(self):
        self.assertEqual(process_ip("192.168..1"), "IP address isn't valid")

    def test_invalid_ip_non_digit_part(self):
        self.assertEqual(process_ip("192.168.a.1"), "IP address isn't valid")

    def test_invalid_ip_out_of_range_part(self):
        self.assertEqual(process_ip("192.168.256.1"), "IP address isn't valid")

    def test_invalid_ip_non_string_input(self):
        self.assertEqual(process_ip(12345), "IP address isn't valid")

    def test_invalid_ip_empty_string(self):
        self.assertEqual(process_ip(""), "IP address isn't valid")

if __name__ == '__main__':
    unittest.main()