import util

def solve(input_path):
  f = open(input_path)
  path1 = f.readline().rstrip()
  path2 = f.readline().rstrip()
  return min(util.manhattan_distances(
    util.intersection_points(
      util.path_to_segments(path1),
      util.path_to_segments(path2))))


if __name__ == '__main__':
    print(solve('input.txt'))
