import unittest

class TestCircuitBreaker(unittest.TestCase):
    def setUp(self):
        self.circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=1.0)

    def test_initial_state(self):
        self.assertEqual(self.circuit_breaker.state, "CLOSED")

    def test_record_failure(self):
        self.circuit_breaker.record_failure()
        self.assertEqual(self.circuit_breaker.state, "CLOSED")
        self.assertEqual(self.circuit_breaker.failures, 1)

    def test_record_failure_threshold(self):
        for _ in range(3):
            self.circuit_breaker.record_failure()
        self.assertEqual(self.circuit_breaker.state, "OPEN")
        self.assertEqual(self.circuit_breaker.failures, 3)

    def test_can_execute_closed(self):
        self.circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=1.0)
        self.assertTrue(self.circuit_breaker.can_execute())

    def test_can_execute_open(self):
        self.circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=1.0)
        for _ in range(3):
            self.circuit_breaker.record_failure()
        self.assertFalse(self.circuit_breaker.can_execute())

    def test_can_execute_half_open(self):
        self.circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=1.0)
        for _ in range(3):
            self.circuit_breaker.record_failure()
        self.circuit_breaker.state = "HALF_OPEN"
        self.assertTrue(self.circuit_breaker.can_execute())

    def test_recovery_timeout(self):
        self.circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=1.0)
        for _ in range(3):
            self.circuit_breaker.record_failure()
        self.assertFalse(self.circuit_breaker.can_execute())
        time.sleep(1.1)
        self.assertTrue(self.circuit_breaker.can_execute())

    def test_record_success(self):
        self.circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=1.0)
        for _ in range(3):
            self.circuit_breaker.record_failure()
        self.circuit_breaker.record_success()
        self.assertEqual(self.circuit_breaker.state, "CLOSED")
        self.assertEqual(self.circuit_breaker.failures, 0)

if __name__ == '__main__':
    unittest.main()
