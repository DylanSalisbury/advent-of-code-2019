import unittest
import util


class UtilTest(unittest.TestCase):

  def test_path_to_segments(self):
    self.assertEqual(
      (
        ((0, 0), (8, 0)),
        ((8, 0), (8, 5)),
        ((8, 5), (3, 5)),
        ((3, 5), (3, 2))),
      util.path_to_segments("R8,U5,L5,D3"))

  def test_intersection_points(self):
    segments1 = util.path_to_segments("R8,U5,L5,D3")
    segments2 = util.path_to_segments("U7,R6,D4,L4")
    expected_intersections = ((3, 3), (6, 5))
    self.assertEqual(sorted(expected_intersections),
                     sorted(util.intersection_points(segments1, segments2)))


  def test_manhattan_distances(self):
    test_cases = (
      ("R8,U5,L5,D3", "U7,R6,D4,L4", 6),
      ("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159),
      ("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", 135)
    )

    for test_case in test_cases:
      self.assertEqual(
        test_case[2],
        min(util.manhattan_distances(
          util.intersection_points(
            util.path_to_segments(test_case[0]),
            util.path_to_segments(test_case[1])))))


  def test_step_distances(self):
    path1 = ("R8,U5,L5,D3")
    path2 = ("U7,R6,D4,L4")
    intersection_points = ((3, 3), (6, 5))
    self.assertEqual(
      (20, 15), util.step_distances(path1, intersection_points))
    self.assertEqual(
      (20, 15), util.step_distances(path2, intersection_points))

    
  def test_min_sum_of_steps(self):
    self.assertEqual(30, util.min_sum_of_steps(
      "R8,U5,L5,D3", "U7,R6,D4,L4"))
    self.assertEqual(610, util.min_sum_of_steps(
      "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"))
    self.assertEqual(410, util.min_sum_of_steps(
      "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))


if __name__ == '__main__':
    unittest.main()
