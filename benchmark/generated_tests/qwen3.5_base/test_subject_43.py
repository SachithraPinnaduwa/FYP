import unittest

class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher(3)

    def test_encrypt_uppercase(self):
        self.assertEqual(self.cipher.encrypt("ABC"), "DEF")

    def test_encrypt_lowercase(self):
        self.assertEqual(self.cipher.encrypt("abc"), "def")

    def test_encrypt_mixed(self):
        self.assertEqual(self.cipher.encrypt("AbC"), "DeF")

    def test_encrypt_special_chars(self):
        self.assertEqual(self.cipher.encrypt("123!@#"), "123!@#")

    def test_decrypt_uppercase(self):
        self.assertEqual(self.cipher.decrypt("DEF"), "ABC")

    def test_decrypt_lowercase(self):
        self.assertEqual(self.cipher.decrypt("def"), "abc")

    def test_decrypt_mixed(self):
        self.assertEqual(self.cipher.decrypt("DeF"), "AbC")

    def test_decrypt_special_chars(self):
        self.assertEqual(self.cipher.decrypt("123!@#"), "123!@#")

    def test_encrypt_decrypt_roundtrip(self):
        text = "Hello, World! 123"
        encrypted = self.cipher.encrypt(text)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, text)

    def test_shift_26(self):
        self.assertEqual(self.cipher.encrypt("ABC"), "ABC")

    def test_shift_0(self):
        self.assertEqual(self.cipher.encrypt("ABC"), "ABC")

    def test_shift_negative(self):
        self.cipher = CaesarCipher(-3)
        self.assertEqual(self.cipher.encrypt("DEF"), "ABC")

if __name__ == "__main__":
    unittest.main()
