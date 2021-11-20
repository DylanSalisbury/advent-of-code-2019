import util

def solve(input_path):
  f = open(input_path)
  path1 = f.readline().rstrip()
  path2 = f.readline().rstrip()
  return util.min_sum_of_steps(path1, path2)


if __name__ == '__main__':
    print(solve('input.txt'))
