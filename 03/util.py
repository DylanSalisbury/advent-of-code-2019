"""Helper functions."""

def path_to_segments(s):
  result = []
  cur_pt = (0, 0)

  for step in s.split(','):
    direction = step[0]
    distance = int(step[1:])
    if direction == 'U':
      next_pt = (cur_pt[0], cur_pt[1] + distance)
    elif direction == 'D':
      next_pt = (cur_pt[0], cur_pt[1] - distance)
    elif direction == 'L':
      next_pt = (cur_pt[0] - distance, cur_pt[1])
    elif direction == 'R':
      next_pt = (cur_pt[0] + distance, cur_pt[1])
    else:
      raise ValueError('Unknown direction ' + direction)
      
    result.append( (cur_pt, next_pt) )
    cur_pt = next_pt

  return tuple(result)


def intersection_points(segments1, segments2):
  result = []
  
  for seg1 in segments1:
    for seg2 in segments2:
      horizontal_seg = None
      vertical_seg = None
      
      for seg in (seg1, seg2):
        if seg[0][0] == seg[1][0]:
          # x vals are the same
          vertical_seg = sorted(seg)
        elif seg[0][1] == seg[1][1]:
          # y vals are the same
          horizontal_seg = sorted(seg)
        else:
          raise ValueError('Segment is neither vertical nor horizontal: ' + str(seg))

      if horizontal_seg and vertical_seg:
        # Both segments are sorted
        y = horizontal_seg[0][1]
        x = vertical_seg[0][0]
        if (x > horizontal_seg[0][0] and x < horizontal_seg[1][0]
            and y > vertical_seg[0][1] and y < vertical_seg[1][1]):
          if x != 0 or y != 0:
            result.append((x, y))

      # Else the lines are parallel and this function ignores the condition where
      # they overlap.

  return tuple(result)


def manhattan_distances(points):
  result = [abs(point[0]) + abs(point[1]) for point in points]
  return tuple(result)


def step_distances(s, intersection_points):
  result = [None] * len(intersection_points)
  cur_pt = [0, 0]

  l = 0
  for step in s.split(','):
    direction = step[0]
    distance = int(step[1:])
    for _ in range(distance):
      l += 1
      if direction == 'U':
        cur_pt[1] += 1
      elif direction == 'D':
        cur_pt[1] -= 1
      elif direction == 'L':
        cur_pt[0] -= 1
      elif direction == 'R':
        cur_pt[0] += 1
      else:
        raise ValueError('Unknown direction ' + direction)

      tp = tuple(cur_pt)
      if tp in intersection_points:
        result[intersection_points.index(tp)] = l

  return tuple(result)  


def min_sum_of_steps(s1, s2):
  points = intersection_points(path_to_segments(s1), path_to_segments(s2))
  distances1 = step_distances(s1, points)
  distances2 = step_distances(s2, points)
  return min([distances1[i] + distances2[i] for i in range(len(distances1))])
