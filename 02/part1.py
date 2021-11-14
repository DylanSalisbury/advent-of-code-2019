import util

def solve(input_path):
  f = open(input_path)
  input_string = f.readline().rstrip()
  storage = util.string_to_list_of_integers(input_string)
  storage[1] = 12
  storage[2] = 2
  util.execute_intcode(storage)
  return storage[0]


if __name__ == '__main__':
    print(solve('input.txt'))
