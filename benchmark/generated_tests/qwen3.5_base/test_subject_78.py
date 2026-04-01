import unittest

class TestBase32Encoder(unittest.TestCase):
    def test_encode_empty(self):
        self.assertEqual(Base32Encoder.encode(b""), "")
    
    def test_encode_single_byte(self):
        self.assertEqual(Base32Encoder.encode(b"A"), "A=")
    
    def test_encode_multiple_bytes(self):
        self.assertEqual(Base32Encoder.encode(b"Hello"), "H=234567")
    
    def test_encode_large_data(self):
        data = b"X" * 1000
        encoded = Base32Encoder.encode(data)
        self.assertEqual(len(encoded), len(data) * 4 // 3 + 1)
    
    def test_encode_with_padding(self):
        data = b"AB"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_multiple(self):
        data = b"ABC"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_three(self):
        data = b"ABCD"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_four(self):
        data = b"ABCDE"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_five(self):
        data = b"ABCDEF"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-5], "=")
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_six(self):
        data = b"ABCDEFG"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-6], "=")
        self.assertEqual(encoded[-5], "=")
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_seven(self):
        data = b"ABCDEFGH"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-7], "=")
        self.assertEqual(encoded[-6], "=")
        self.assertEqual(encoded[-5], "=")
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_eight(self):
        data = b"ABCDEFGHI"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-8], "=")
        self.assertEqual(encoded[-7], "=")
        self.assertEqual(encoded[-6], "=")
        self.assertEqual(encoded[-5], "=")
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_nine(self):
        data = b"ABCDEFGHIJ"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-9], "=")
        self.assertEqual(encoded[-8], "=")
        self.assertEqual(encoded[-7], "=")
        self.assertEqual(encoded[-6], "=")
        self.assertEqual(encoded[-5], "=")
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_ten(self):
        data = b"ABCDEFGHIJK"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-10], "=")
        self.assertEqual(encoded[-9], "=")
        self.assertEqual(encoded[-8], "=")
        self.assertEqual(encoded[-7], "=")
        self.assertEqual(encoded[-6], "=")
        self.assertEqual(encoded[-5], "=")
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_eleven(self):
        data = b"ABCDEFGHIJKL"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-11], "=")
        self.assertEqual(encoded[-10], "=")
        self.assertEqual(encoded[-9], "=")
        self.assertEqual(encoded[-8], "=")
        self.assertEqual(encoded[-7], "=")
        self.assertEqual(encoded[-6], "=")
        self.assertEqual(encoded[-5], "=")
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_twelve(self):
        data = b"ABCDEFGHIJKLM"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-12], "=")
        self.assertEqual(encoded[-11], "=")
        self.assertEqual(encoded[-10], "=")
        self.assertEqual(encoded[-9], "=")
        self.assertEqual(encoded[-8], "=")
        self.assertEqual(encoded[-7], "=")
        self.assertEqual(encoded[-6], "=")
        self.assertEqual(encoded[-5], "=")
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_thirteen(self):
        data = b"ABCDEFGHIJKLMN"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-13], "=")
        self.assertEqual(encoded[-12], "=")
        self.assertEqual(encoded[-11], "=")
        self.assertEqual(encoded[-10], "=")
        self.assertEqual(encoded[-9], "=")
        self.assertEqual(encoded[-8], "=")
        self.assertEqual(encoded[-7], "=")
        self.assertEqual(encoded[-6], "=")
        self.assertEqual(encoded[-5], "=")
        self.assertEqual(encoded[-4], "=")
        self.assertEqual(encoded[-3], "=")
        self.assertEqual(encoded[-2], "=")
        self.assertEqual(encoded[-1], "=")
    
    def test_encode_with_padding_fourteen(self):
        data = b"ABCDEFGHIJKLMNO"
        encoded = Base32Encoder.encode(data)
        self.assertEqual(encoded[-14], "=")
        self.assertEqual(encoded[-13], "=")
        self.assertEqual(encoded[-12], "=")