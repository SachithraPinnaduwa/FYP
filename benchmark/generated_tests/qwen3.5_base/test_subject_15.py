import unittest

class TestSimpleJWT(unittest.TestCase):
    def setUp(self):
        self.jwt = SimpleJWT("secret_key")

    def test_sign_and_verify(self):
        payload = {"user_id": 123, "role": "admin"}
        token = self.jwt.sign(payload)
        result = self.jwt.verify(token)
        self.assertEqual(result, payload)

    def test_expired_token(self):
        payload = {"user_id": 123, "role": "admin"}
        token = self.jwt.sign(payload, exp_in_seconds=-1)
        result = self.jwt.verify(token)
        self.assertIsNone(result)

    def test_invalid_token(self):
        token = "invalid.token"
        result = self.jwt.verify(token)
        self.assertIsNone(result)

    def test_missing_exp(self):
        payload = {"user_id": 123, "role": "admin"}
        token = self.jwt.sign(payload)
        del payload["exp"]
        token = self.jwt.sign(payload)
        result = self.jwt.verify(token)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
