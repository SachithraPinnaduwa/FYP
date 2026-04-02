import unittest

class TestFactorial(unittest.TestCase):
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_2(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_3(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_4(self):
        self.assertEqual(factorial(4), 24)

    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_6(self):
        self.assertEqual(factorial(6), 720)

    def test_factorial_7(self):
        self.assertEqual(factorial(7), 5040)

    def test_factorial_8(self):
        self.assertEqual(factorial(8), 40320)

    def test_factorial_9(self):
        self.assertEqual(factorial(9), 362880)

    def test_factorial_10(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_11(self):
        self.assertEqual(factorial(11), 39916800)

    def test_factorial_12(self):
        self.assertEqual(factorial(12), 479001600)

    def test_factorial_13(self):
        self.assertEqual(factorial(13), 6227020800)

    def test_factorial_14(self):
        self.assertEqual(factorial(14), 87178291200)

    def test_factorial_15(self):
        self.assertEqual(factorial(15), 1307674368000)

    def test_factorial_16(self):
        self.assertEqual(factorial(16), 20922789888000)

    def test_factorial_17(self):
        self.assertEqual(factorial(17), 355687428096000)

    def test_factorial_18(self):
        self.assertEqual(factorial(18), 6402373705728000)

    def test_factorial_19(self):
        self.assertEqual(factorial(19), 121645100408832000)

    def test_factorial_20(self):
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_factorial_21(self):
        self.assertEqual(factorial(21), 51090942171709440000)

    def test_factorial_22(self):
        self.assertEqual(factorial(22), 1124000727777607680000)

    def test_factorial_23(self):
        self.assertEqual(factorial(23), 2432902008176640000)

    def test_factorial_24(self):
        self.assertEqual(factorial(24), 620448401733239439360000)

    def test_factorial_25(self):
        self.assertEqual(factorial(25), 15511210043330985984000000)

    def test_factorial_26(self):
        self.assertEqual(factorial(26), 403291461126605635584000000)

    def test_factorial_27(self):
        self.assertEqual(factorial(27), 10888869450418352160768000000)

    def test_factorial_28(self):
        self.assertEqual(factorial(28), 3008720093991362972800000000)

    def test_factorial_29(self):
        self.assertEqual(factorial(29), 9084539500000000000000000000)

    def test_factorial_30(self):
        self.assertEqual(factorial(30), 27041561800000000000000000000)

    def test_factorial_31(self):
        self.assertEqual(factorial(31), 82928841580000000000000000000)

    def test_factorial_32(self):
        self.assertEqual(factorial(32), 26214420000000000000000000000)

    def test_factorial_33(self):
        self.assertEqual(factorial(33), 8683142400000000000000000000)

    def test_factorial_34(self):
        self.assertEqual(factorial(34), 2952368416000000000000000000)

    def test_factorial_35(self):
        self.assertEqual(factorial(35), 1018069400000000000000000000)

    def test_factorial_36(self):
        self.assertEqual(factorial(36), 366504984000000000000000000)

    def test_factorial_37(self):
        self.assertEqual(factorial(37), 135606844000000000000000000)

    def test_factorial_38(self):
        self.assertEqual(factorial(38), 51530590000000000000000000)

    def test_factorial_39(self):