import unittest, importlib

fraction = importlib.import_module("01-introduction.fraction")
# from introduction.fraction import Fraction
Fraction = getattr(fraction, "Fraction")


class TestFraction(unittest.TestCase):
    def test_init(self):
        num = 12
        den = 8

        result = Fraction(num, den)
        self.assertIsInstance(result, Fraction)
        self.assertEqual(result.num, 3)
        self.assertEqual(result.den, 2)

        result = Fraction(-num, den)
        self.assertEqual(result.num, -3)
        self.assertEqual(result.den, 2)

        result = Fraction(num, -den)
        self.assertEqual(result.num, -3)
        self.assertEqual(result.den, 2)

        result = Fraction(-num, -den)
        self.assertEqual(result.num, 3)
        self.assertEqual(result.den, 2)

    def test_add(self):
        self.assertEqual(Fraction(3, 4), Fraction(1, 4) + Fraction(2, 4))
        self.assertEqual(Fraction(-1, 3), Fraction(-3, 3) + Fraction(2, 3))
        self.assertEqual(Fraction(-4, 5), Fraction(-2, 10) + Fraction(-6, 10))

    def test_sub(self):
        self.assertEqual(Fraction(1, 4), Fraction(3, 4) - Fraction(2, 4))
        self.assertEqual(Fraction(-5, 3), Fraction(-3, 3) - Fraction(2, 3))
        self.assertEqual(Fraction(2, 5), Fraction(-2, 10) - Fraction(-6, 10))

    def test_mul(self):
        self.assertEqual(Fraction(1, 6), Fraction(1, 3) * Fraction(2, 4))
        self.assertEqual(Fraction(-2, 3), Fraction(-3, 3) * Fraction(2, 3))
        self.assertEqual(Fraction(1, 1), Fraction(-2, 4) * Fraction(-6, 3))

    def test_truediv(self):
        self.assertEqual(Fraction(4, 6), Fraction(1, 3) / Fraction(2, 4))
        self.assertEqual(Fraction(-9, 6), Fraction(-3, 3) / Fraction(2, 3))
        self.assertEqual(Fraction(-6, -24), Fraction(-2, 4) / Fraction(-6, 3))

    def test_eq(self):
        self.assertEqual(Fraction(1, 3), Fraction(2, 6))
        self.assertEqual(Fraction(-2, 4), Fraction(2, -4))
        self.assertEqual(Fraction(6, 2), Fraction(-3, -1))

    def test_str(self):
        self.assertEqual(str(Fraction(-6, -3)), "2/1")


if __name__ == "__main__":
    unittest.main()