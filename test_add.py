import unittest
from add import add

class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_add_decimal_numbers(self):
        self.assertEqual(add(2.5, 1.5), 4.0)

if __name__ == '__main__':
    unittest.main()