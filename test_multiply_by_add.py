import unittest
from multiply_by_add import multiply_by_add

class TestMultiplyByAdd(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply_by_add(4, 3), 12)

    def test_zero(self):
        self.assertEqual(multiply_by_add(5, 0), 0)

    def test_one(self):
        self.assertEqual(multiply_by_add(7, 1), 7)

if __name__ == '__main__':
    unittest.main()