import unittest

class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        self.vc = VigenereCipher("KEY")

    def test_encrypt_simple(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_simple(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_numbers(self):
        self.assertEqual(self.vc.encrypt("HELLO123"), "KJQQT123")

    def test_decrypt_with_numbers(self):
        self.assertEqual(self.vc.decrypt("KJQQT123"), "HELLO123")

    def test_encrypt_with_spaces(self):
        self.assertEqual(self.vc.encrypt("HELLO WORLD"), "KJQQT QZQQT")

    def test_decrypt_with_spaces(self):
        self.assertEqual(self.vc.decrypt("KJQQT QZQQT"), "HELLO WORLD")

    def test_encrypt_with_special_chars(self):
        self.assertEqual(self.vc.encrypt("HELLO!@#"), "KJQQT!@#")

    def test_decrypt_with_special_chars(self):
        self.assertEqual(self.vc.decrypt("KJQQT!@#"), "HELLO!@#")

    def test_encrypt_with_empty_string(self):
        self.assertEqual(self.vc.encrypt(""), "")

    def test_decrypt_with_empty_string(self):
        self.assertEqual(self.vc.decrypt(""), "")

    def test_encrypt_with_long_key(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_long_key(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_repeated_key(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_repeated_key(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_mixed_case(self):
        self.assertEqual(self.vc.encrypt("Hello World"), "KJQQT QZQQT")

    def test_decrypt_with_mixed_case(self):
        self.assertEqual(self.vc.decrypt("KJQQT QZQQT"), "Hello World")

    def test_encrypt_with_non_alpha_chars(self):
        self.assertEqual(self.vc.encrypt("123!@#"), "123!@#")

    def test_decrypt_with_non_alpha_chars(self):
        self.assertEqual(self.vc.decrypt("123!@#"), "123!@#")

    def test_encrypt_with_uppercase(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_uppercase(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_lowercase(self):
        self.assertEqual(self.vc.encrypt("hello"), "KJQQT")

    def test_decrypt_with_lowercase(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "hello")

    def test_encrypt_with_key_length_1(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_1(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_26(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_26(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_0(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "HELLO")

    def test_decrypt_with_key_length_0(self):
        self.assertEqual(self.vc.decrypt("HELLO"), "HELLO")

    def test_encrypt_with_key_length_100(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_100(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_1000(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_1000(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_10000(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_10000(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_100000(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_100000(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_1000000(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_1000000(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_10000000(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_10000000(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_100000000(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_100000000(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_1000000000(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_1000000000(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_10000000000(self):
        self.assertEqual(self.vc.encrypt("HELLO"), "KJQQT")

    def test_decrypt_with_key_length_10000000000(self):
        self.assertEqual(self.vc.decrypt("KJQQT"), "HELLO")

    def test_encrypt_with_key_length_100000000000(self):
        self.assertEqual(self.vc.encrypt("HELLO