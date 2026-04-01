import unittest

class TestLeakyBucketLimiter(unittest.TestCase):
    def test_initial_state(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=1.0)
        self.assertEqual(limiter.current_level, 0.0)
        self.assertEqual(limiter.last_update, time.monotonic())

    def test_allow_request_within_capacity(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=1.0)
        self.assertTrue(limiter.allow_request(drop_size=5.0))
        self.assertEqual(limiter.current_level, 5.0)

    def test_allow_request_exceeds_capacity(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=1.0)
        self.assertTrue(limiter.allow_request(drop_size=5.0))
        self.assertFalse(limiter.allow_request(drop_size=6.0))
        self.assertEqual(limiter.current_level, 5.0)

    def test_leak_rate_decreases_level(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=1.0)
        self.assertTrue(limiter.allow_request(drop_size=5.0))
        time.sleep(0.1)  # Simulate time passing
        self.assertLess(limiter.current_level, 5.0)

    def test_leak_rate_does_not_go_below_zero(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=1.0)
        self.assertTrue(limiter.allow_request(drop_size=5.0))
        time.sleep(0.2)  # Simulate time passing
        self.assertGreaterEqual(limiter.current_level, 0.0)

    def test_allow_request_with_zero_drop_size(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=1.0)
        self.assertTrue(limiter.allow_request(drop_size=0.0))
        self.assertEqual(limiter.current_level, 0.0)

    def test_allow_request_with_large_drop_size(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=1.0)
        self.assertFalse(limiter.allow_request(drop_size=100.0))
        self.assertEqual(limiter.current_level, 0.0)

    def test_allow_request_with_negative_drop_size(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=1.0)
        self.assertFalse(limiter.allow_request(drop_size=-1.0))
        self.assertEqual(limiter.current_level, 0.0)

    def test_allow_request_with_zero_capacity(self):
        limiter = LeakyBucketLimiter(capacity=0.0, leak_rate=1.0)
        self.assertFalse(limiter.allow_request(drop_size=1.0))
        self.assertEqual(limiter.current_level, 0.0)

    def test_allow_request_with_zero_leak_rate(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=0.0)
        self.assertTrue(limiter.allow_request(drop_size=5.0))
        self.assertEqual(limiter.current_level, 5.0)
        time.sleep(0.1)  # Simulate time passing
        self.assertEqual(limiter.current_level, 5.0)

    def test_allow_request_with_high_leak_rate(self):
        limiter = LeakyBucketLimiter(capacity=10.0, leak_rate=10.0)
        self.assertTrue(limiter.allow_request(drop_size=5.0))
        time.sleep(0.1)  # Simulate time passing
        self.assertLess(limiter.current_level, 5.0)

    def test_allow_request_with_high_capacity(self):
        limiter = LeakyBucketLimiter(capacity=100.0, leak_rate=1.0)
        self.assertTrue(limiter.allow_request(drop_size=50.0))
        self.assertTrue(limiter.allow_request(drop_size=50.0))
        self.assertEqual(limiter.current_level, 100.0)

    def test_allow_request_with_high_leak_rate_and_high_capacity(self):
        limiter = LeakyBucketLimiter(capacity=100.0, leak_rate=10.0)
        self.assertTrue(limiter.allow_request(drop_size=50.0))
        time.sleep(0.1)  # Simulate time passing
        self.assertLess(limiter.current_level, 50.0)

    def test_allow_request_with_high_leak_rate_and_high_capacity_and_high_drop_size(self):
        limiter = LeakyBucketLimiter(capacity=100.0, leak_rate=10.0)
        self.assertTrue(limiter.allow_request(drop_size=50.0))
        time.sleep(0.1)  # Simulate time passing
        self.assertFalse(limiter.allow_request(drop_size=50.0))
        self.assertLess(limiter.current_level, 50.0)

    def test_allow_request_with_high_leak_rate_and_high_capacity_and_high_drop_size_and_high_capacity(self):
        limiter = LeakyBucketLimiter(capacity=100.0, leak_rate=10.0)
        self.assertTrue(limiter.allow_request(drop_size=50.0))
        time.sleep(0.1)  # Simulate time passing
        self.assertFalse(limiter.allow_request(drop_size=50.0))
        self.assertLess(limiter.current_level, 50.0)
        self.assertTrue(limiter.allow_request(drop_size=50.0))
        self.assertEqual(limiter.current_level, 100.0)

    def test_allow_request_with_high_leak_rate_and_high_capacity_and_high_drop_size_and_high_capacity_and_high_leak_rate(self):
        limiter = LeakyBucketLimiter(capacity=100.0, leak_rate=10.0)
        self.assertTrue(limiter.allow_request(drop_size=50.0))
        time.sleep(0.1)  # Simulate time passing
        self.assertFalse(limiter.allow_request(drop_size=50.0))
        self.assertLess(limiter.current_level, 50.0)
        self.assertTrue(limiter.allow_request(drop_size=50.0))
        self.assertEqual(limiter.current_level, 100.0)
        time.sleep(0.1)  # Simulate time passing
        self.assertFalse(limiter.allow_request(drop_size=50.0))
        self.assertLess(limiter.current_level, 50.0)
        self.assertTrue(limiter.allow_request(drop_size=50.0))
        self.assertEqual(limiter.current_level, 100.0)
        time.sleep(0.1)  # Simulate time passing
        self.assertFalse(limiter.allow_request(drop_size=50.0))
        self.assertLess(limiter.current_level, 50.0)
        self.assertTrue(limiter.allow_request(drop_size=50.0))