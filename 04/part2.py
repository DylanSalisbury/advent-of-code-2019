import util

def solve(input_path):
  with open(input_path) as f:
    input_str = f.readline().rstrip()
    begin_end_text = input_str.split('-')
    begin = int(begin_end_text[0])
    end = int(begin_end_text[1])
  return util.solve(begin, end, util.part2_filter)


if __name__ == '__main__':
    print(solve('input.txt'))
