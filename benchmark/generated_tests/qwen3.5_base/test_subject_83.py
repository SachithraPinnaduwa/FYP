import unittest

class TestTokenBucket(unittest.TestCase):
    def test_initial_tokens(self):
        bucket = TokenBucket(capacity=10, refill_rate=1.0)
        self.assertEqual(bucket.tokens, 10.0)

    def test_consume_success(self):
        bucket = TokenBucket(capacity=10, refill_rate=1.0)
        self.assertTrue(bucket.consume(3))
        self.assertEqual(bucket.tokens, 7.0)

    def test_consume_failure(self):
        bucket = TokenBucket(capacity=10, refill_rate=1.0)
        self.assertFalse(bucket.consume(15))
        self.assertEqual(bucket.tokens, 10.0)

    def test_refill(self):
        bucket = TokenBucket(capacity=10, refill_rate=1.0)
        bucket.consume(10)
        self.assertEqual(bucket.tokens, 0.0)
        import time
        time.sleep(0.5)
        self.assertGreater(bucket.tokens, 0.0)

    def test_time_until_next_token(self):
        bucket = TokenBucket(capacity=10, refill_rate=1.0)
        bucket.consume(10)
        self.assertEqual(bucket.time_until_next_token(), 0.0)
        bucket.consume(10)
        self.assertEqual(bucket.time_until_next_token(), 0.0)
        import time
        time.sleep(0.5)
        self.assertGreater(bucket.time_until_next_token(), 0.0)

if __name__ == '__main__':
    unittest.main()
