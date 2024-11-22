import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
  def setUp(self):
    self.calc = SimpleCalculator()

  def test_addition(self):
    self.assertEqual(self.calc.add(4, 6), 10)

  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(7, 3), 4)

  def test_multiplication(self):
    self.assertEqual(self.calc.multiply(3, 4), 12)

  def test_divide(self):
    self.assertEqual(self.calc.divide(3, 0), None)


if __name__ == "__main__":
  unittest.main()