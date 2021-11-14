import unittest
import util

# Even though the code operates on (mutable) lists, it's good to use
# immutable types for this data, to be assured that the code won't
# accidentally change it.
TEST_CASES = (
  ("1,0,0,0,99", (2,0,0,0,99)),
  ("2,3,0,3,99", (2,3,0,6,99)),
  ("2,4,4,5,99,0", (2,4,4,5,99,9801)),
  ("1,1,1,4,99,5,6,0,99", (30,1,1,4,2,5,6,0,99))
)


class UtilTest(unittest.TestCase):

  def test_string_to_list_of_integers(self):
    l = util.string_to_list_of_integers("0, 1, 2, 3")
    self.assertEqual(list, type(l))
    self.assertEqual(4, len(l))
    self.assertEqual(0, l[0])
    self.assertEqual(1, l[1])
    self.assertEqual(2, l[2])
    self.assertEqual(3, l[3])

  def test_execute_intcode(self):
    for test_case in TEST_CASES:
      storage = util.string_to_list_of_integers(test_case[0])
      util.execute_intcode(storage)  # Modifies storage
      self.assertEqual(test_case[1], tuple(storage))

      
if __name__ == '__main__':
    unittest.main()


