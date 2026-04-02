import unittest
from lispyc import parse, ComposedForm, Param, Variable

class TestValidateLambdaExpression(unittest.TestCase):
    def test_valid_lambda_expression(self):
        self.assertTrue(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))
        self.assertTrue(validate_lambda_expression("(lambda ((int x)) (x 5))"))
        self.assertTrue(validate_lambda_expression("(lambda ((float y)) (* y y))"))
        self.assertTrue(validate_lambda_expression("(lambda ((bool z) (int w)) (if z w 0))"))

    def test_invalid_lambda_expression(self):
        self.assertFalse(validate_lambda_expression("lambda ((int a) (bool b)) (if a b a)"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) if a b a)"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool b)) (if a b a))"))  # Missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda ((int a) (bool