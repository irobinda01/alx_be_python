import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
  def test_add(self):
    cal = SimpleCalculator()
    result = cal.add(5, 6)
    self.assertEqual(result, 11)

  def test_subtract(self):
    cal = SimpleCalculator()
    result = cal.subtract(7, 4)
    self.assertEqual(result, 3)

  def test_multiply(self):
    cal = SimpleCalculator()
    result = cal.multiply(3, 4)
    self.assertEqual(result, 12)

  def test_divide(self):
    cal = SimpleCalculator()
    result = cal.divide(4, 0)
    self.assertEqual(result, None)


if __name__ == "__main__":
  unittest.main()