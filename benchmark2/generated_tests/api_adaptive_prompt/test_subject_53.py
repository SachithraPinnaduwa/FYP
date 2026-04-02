from subject_53 import *

```python
import unittest
from lispyc import parse, ComposedForm, Param, Variable

class TestValidateLambdaExpression(unittest.TestCase):
    def test_valid_lambda_expression(self):
        self.assertTrue(validate_lambda_expression("(lambda (int x) x)"))
        self.assertTrue(validate_lambda_expression("(lambda (bool y) (not y))"))
        self.assertTrue(validate_lambda_expression("(lambda (float z) (* z 2))"))
        self.assertTrue(validate_lambda_expression("(lambda (int a int b) (+ a b))"))

    def test_invalid_lambda_expression(self):
        self.assertFalse(validate_lambda_expression("(lambda (int x)"))
        self.assertFalse(validate_lambda_expression("(lambda (int x y) x)"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (int y))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (not y))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (+ a b))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (* a))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o p))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o p q))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o p q r))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o p q r s))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o p q r s t))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o p q r s t u))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o p q r s t u v))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o p q r s t u v w))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o p q r s t u v w x))"))
        self.assertFalse(validate_lambda_expression("(lambda (int x) (x y z a b c d e f g h i j k l m n o