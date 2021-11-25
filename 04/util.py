"""Helper functions."""

# Given a number, finds the next number that meets
# criteria 4 (digits never decrease).
#
# Returns that number and whether or not the new
# number meets criteria 3 (two adjacent digits are the same)

def part1_inc(n):
  digits = list(str(n + 1))
  will_succeed = False
  for i in range(1, len(digits)):
    if digits[i] <= digits[i - 1]:
      will_succeed = True
    if digits[i] < digits[i - 1]:
      for j in range(i, len(digits)):
        digits[j] = digits[i - 1]

  # This is an optimization, but makes it hard to define
  # and function's behavior succinctly.
  #
  # if not will_succeed:
  #   digits[len(digits) - 1] = '9'

  return (int(''.join(digits)), will_succeed)


def solve(begin, end, extra_filter):
  n = begin

  result = 0
  while (n <= end):
    z = part1_inc(n)
    if z[1] and z[0] <= end:
      if not extra_filter or extra_filter(z[0]):
        result += 1
    n = z[0]

  return result


def part2_filter(n):
  digits = list(str(n))
  for i in range(1, len(digits)):
    if (
      digits[i] == digits[i-1]
      and (i == 1 or digits[i-1] != digits[i-2])
      and (i == len(digits) - 1 or digits[i] != digits[i+1])):
      return True
  return False
