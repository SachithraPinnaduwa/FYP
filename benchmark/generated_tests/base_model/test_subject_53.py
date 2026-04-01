import unittest
from lispyc.parser import parse, ComposedForm, Param, Variable

class TestValidateLambdaExpression(unittest.TestCase):

    def test_valid_lambda_expression(self):
        self.assertTrue(validate_lambda_expression("(lambda (int x bool y) (+ x y))"))

    def test_invalid_lambda_expression_missing_parentheses(self):
        self.assertFalse(validate_lambda_expression("lambda (int x bool y) (+ x y)"))

    def test_invalid_lambda_expression_no_parameters(self):
        self.assertFalse(validate_lambda_expression("(lambda () (+ x y))"))

    def test_invalid_lambda_expression_invalid_type(self):
        self.assertFalse(validate_lambda_expression("(lambda (string x int y) (+ x y))"))

    def test_invalid_lambda_expression_non_param_in_parameters(self):
        self.assertFalse(validate_lambda_expression("(lambda (int x bool y) (+ x z))"))

    def test_invalid_lambda_expression_body_not_expression(self):
        self.assertFalse(validate_lambda_expression("(lambda (int x bool y) x y)"))

    def test_invalid_lambda_expression_extra_elements(self):
        self.assertFalse(validate_lambda_expression("(lambda (int x bool y) (+ x y) (* x y))"))

if __name__ == '__main__':
    unittest.main()