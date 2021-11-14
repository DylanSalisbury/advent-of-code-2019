"""Helper functions."""

def mass_to_fuel(m):
  f = int(m/3)-2

  if f < 0:
    return 0

  return f

def compound_mass_to_fuel(m):
  f = mass_to_fuel(m)

  if f == 0:
    return f

  return f + compound_mass_to_fuel(f)

