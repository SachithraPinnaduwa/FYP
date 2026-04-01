import unittest

class TestBloomFilter(unittest.TestCase):
    def test_add_and_check(self):
        bf = BloomFilter(1000, 0.01)
        bf.add("item1")
        self.assertTrue(bf.check("item1"))
        self.assertFalse(bf.check("item2"))

    def test_add_multiple_items(self):
        bf = BloomFilter(1000, 0.01)
        for i in range(10):
            bf.add(f"item{i}")
        for i in range(10):
            self.assertTrue(bf.check(f"item{i}"))
        self.assertFalse(bf.check("item100"))

    def test_add_duplicate_items(self):
        bf = BloomFilter(1000, 0.01)
        bf.add("item1")
        bf.add("item1")
        self.assertTrue(bf.check("item1"))

    def test_add_non_string_items(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(123)
        self.assertTrue(bf.check(123))

    def test_add_empty_string(self):
        bf = BloomFilter(1000, 0.01)
        bf.add("")
        self.assertTrue(bf.check(""))

    def test_add_unicode_string(self):
        bf = BloomFilter(1000, 0.01)
        bf.add("日本語")
        self.assertTrue(bf.check("日本語"))

    def test_add_special_characters(self):
        bf = BloomFilter(1000, 0.01)
        bf.add("special!@#$%^&*()")
        self.assertTrue(bf.check("special!@#$%^&*()"))

    def test_add_large_number(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(1234567890)
        self.assertTrue(bf.check(1234567890))

    def test_add_negative_number(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(-1234567890)
        self.assertTrue(bf.check(-1234567890))

    def test_add_float(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(123.456)
        self.assertTrue(bf.check(123.456))

    def test_add_list(self):
        bf = BloomFilter(1000, 0.01)
        bf.add([1, 2, 3])
        self.assertTrue(bf.check([1, 2, 3]))

    def test_add_tuple(self):
        bf = BloomFilter(1000, 0.01)
        bf.add((1, 2, 3))
        self.assertTrue(bf.check((1, 2, 3)))

    def test_add_dict(self):
        bf = BloomFilter(1000, 0.01)
        bf.add({"key": "value"})
        self.assertTrue(bf.check({"key": "value"}))

    def test_add_set(self):
        bf = BloomFilter(1000, 0.01)
        bf.add({1, 2, 3})
        self.assertTrue(bf.check({1, 2, 3}))

    def test_add_none(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(None)
        self.assertTrue(bf.check(None))

    def test_add_bytes(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"item")
        self.assertTrue(bf.check(b"item"))

    def test_add_bytes_with_unicode(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"日本語")
        self.assertTrue(bf.check(b"日本語"))

    def test_add_bytes_with_special_characters(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"special!@#$%^&*()")
        self.assertTrue(bf.check(b"special!@#$%^&*()"))

    def test_add_bytes_with_large_number(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"1234567890")
        self.assertTrue(bf.check(b"1234567890"))

    def test_add_bytes_with_negative_number(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"-1234567890")
        self.assertTrue(bf.check(b"-1234567890"))

    def test_add_bytes_with_float(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"123.456")
        self.assertTrue(bf.check(b"123.456"))

    def test_add_bytes_with_list(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"[1, 2, 3]")
        self.assertTrue(bf.check(b"[1, 2, 3]"))

    def test_add_bytes_with_tuple(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"(1, 2, 3)")
        self.assertTrue(bf.check(b"(1, 2, 3)"))

    def test_add_bytes_with_dict(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b'{"key": "value"}')
        self.assertTrue(bf.check(b'{"key": "value"}'))

    def test_add_bytes_with_set(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"{1, 2, 3}")
        self.assertTrue(bf.check(b"{1, 2, 3}"))

    def test_add_bytes_with_none(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"None")
        self.assertTrue(bf.check(b"None"))

    def test_add_bytes_with_empty_string(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"")
        self.assertTrue(bf.check(b""))

    def test_add_bytes_with_unicode(self):
        bf = BloomFilter(1000, 0.01)
        bf.add(b"