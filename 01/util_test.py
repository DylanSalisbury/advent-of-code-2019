import unittest
import util

class UtilTest(unittest.TestCase):

  def test_mass_to_fuel(self):
    self.assertEqual(2, util.mass_to_fuel(12))
    self.assertEqual(2, util.mass_to_fuel(14))
    self.assertEqual(654, util.mass_to_fuel(1969))
    self.assertEqual(33583, util.mass_to_fuel(100756))

  def test_mass_to_fuel_not_negative(self):
    self.assertEqual(0, util.mass_to_fuel(1))

  def test_compound_mass_to_fuel(self):
    self.assertEqual(2, util.compound_mass_to_fuel(14))
    self.assertEqual(966, util.compound_mass_to_fuel(1969))
    self.assertEqual(50346, util.compound_mass_to_fuel(100756))
    
if __name__ == '__main__':
    unittest.main()


