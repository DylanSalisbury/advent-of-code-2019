import unittest
import util

class UtilTest(unittest.TestCase):

  def test_part1_inc(self):
    test_cases = (
      (1200, (1222, True)),
      (1222, (1223, True)),
      (1223, (1224, True)),
      (1229, (1233, True)),
      (1233, (1234, False)),
      (1239, (1244, True)),
      (1244, (1245, False)),
    )
    for test_case in test_cases:
      self.assertEqual(test_case[1], util.part1_inc(test_case[0]))


if __name__ == '__main__':
    unittest.main()


