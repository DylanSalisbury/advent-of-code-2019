import util

def attempt(input_path, noun, verb):
  f = open(input_path)
  input_string = f.readline().rstrip()
  storage = util.string_to_list_of_integers(input_string)
  storage[1] = noun
  storage[2] = verb
  util.execute_intcode(storage)
  return storage[0]


def solve(input_path):
  for noun in range(100):
    for verb in range(100):
      if attempt('input.txt', noun, verb) == 19690720:
        return 100 * noun + verb
  raise ValueError("Couldn't find suitable noun and verb")


if __name__ == '__main__':
    print(solve('input.txt'))

