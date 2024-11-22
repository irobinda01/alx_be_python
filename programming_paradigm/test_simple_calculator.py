import unittest
from simple_calculator import addition, subtraction, multiplication, division

class TestSimpleCalculator(unittest.TestCase):
  def test_addition(self):
    self.assertEqual(addition(2, 5), 7)

  def test_subtraction(self):
    self.assertEqual(subtraction(7, 3), 4)

  def test_multiply(self):
    self.assertEqual(multiplication(3, 4), 12)

  def test_divide(self):
    self.assertEqual(division(4, 0), None)


if __name__ == "__main__":
  unittest.main()