import unittest
from exponent import power

class TestExponent(unittest.TestCase):

    def test_power_positive_numbers(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_negative_base(self):
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, 2), 4)

    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -2), 0.25)

    def test_power_by_zero(self):
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)

    def test_power_decimal_numbers(self):
        self.assertEqual(power(4, 0.5), 2.0) 

if __name__ == '__main__':
    unittest.main()