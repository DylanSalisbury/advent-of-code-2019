import util

def solve(input_path):
  f = open(input_path)
  total_fuel = 0
  for m in f:
    total_fuel += util.mass_to_fuel(int(m.rstrip()))

  return total_fuel

if __name__ == '__main__':
    print(solve('input.txt'))
