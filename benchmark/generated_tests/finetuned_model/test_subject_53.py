import unittest
from lispyc.parse import parse
from lispyc.types import Param, Variable, ComposedForm

class TestValidateLambdaExpression(unittest.TestCase):

    def test_valid_lambda_expression(self):
        # Test a valid lambda expression
        self.assertTrue(validate_lambda_expression("(lambda (int x) (int + x 1))"))

    def test_invalid_lambda_expression_missing_type(self):
        # Test a lambda expression with a missing type
        self.assertFalse(validate_lambda_expression("(lambda (x) (int + x 1))"))

    def test_invalid_lambda_expression_missing_variable(self):
        # Test a lambda expression with a missing variable
        self.assertFalse(validate_lambda_expression("(lambda (int) (int + 1 1))"))

    def test_invalid_lambda_expression_missing_body(self):
        # Test a lambda expression with a missing body
        self.assertFalse(validate_lambda_expression("(lambda (int x))"))

    def test_invalid_lambda_expression_extra_parameters(self):
        # Test a lambda expression with extra parameters
        self.assertFalse(validate_lambda_expression("(lambda (int x int y) (int + x y))"))

    def test_invalid_lambda_expression_extra_body(self):
        # Test a lambda expression with extra body
        self.assertFalse(validate_lambda_expression("(lambda (int x) (int + x 1 int y))"))

    def test_invalid_lambda_expression_invalid_type(self):
        # Test a lambda expression with an invalid type
        self.assertFalse(validate_lambda_expression("(lambda (int x) (int + x string y))"))

    def test_invalid_lambda_expression_invalid_variable(self):
        # Test a lambda expression with an invalid variable
        self.assertFalse(validate_lambda_expression("(lambda (int x) (int + x 1))"))

    def test_invalid_lambda_expression_invalid_body(self):
        # Test a lambda expression with an invalid body
        self.assertFalse(validate_lambda_expression("(lambda (int x) (int + x 1 int y))"))

    def test_invalid_lambda_expression_empty_parameters(self):
        # Test a lambda expression with empty parameters
        self.assertFalse(validate_lambda_expression("(lambda () (int + 1 1))"))

    def test_invalid_lambda_expression_empty_body(self):
        # Test a lambda expression with empty body
        self.assertFalse(validate_lambda_expression("(lambda (int x) ())"))

    def test_invalid_lambda_expression_invalid_expression(self):
        # Test a lambda expression with an invalid expression
        self.assertFalse(validate_lambda_expression("(lambda (int x) (int + 1 1 int y))"))

    def test_invalid_lambda_expression_missing_parentheses(self):
        # Test a lambda expression missing parentheses
        self.assertFalse(validate_lambda_expression("(lambda (int x) (int + x 1))"))