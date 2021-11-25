import util

def solve(input_path):
  f = open(input_path)
  input_str = f.readline().rstrip()
  begin_end_text = input_str.split('-')
  n = int(begin_end_text[0]) - 1
  end = int(begin_end_text[1])
  result = 0
  while (n <= end):
    z = util.part1_inc(n)
    if z[1] and z[0] <= end:
      result += 1
    n = z[0]

  return result

      
if __name__ == '__main__':
    print(solve('input.txt'))
