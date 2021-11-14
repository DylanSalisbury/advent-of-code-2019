"""Helper functions."""

def string_to_list_of_integers(s):
  return [int(n) for n in s.split(',')]


def execute_intcode(l):
  i = 0
  while l[i] != 99:
    if l[i] == 1:
      l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
    elif l[i] == 2:
      l[l[i+3]] = l[l[i+1]] * l[l[i+2]]
    else:
      raise ValueError('Unknown opcode ' + l[i])
    i += 4
  return
