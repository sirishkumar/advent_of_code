with open("input.txt") as fp:
  prev_depth = None
  depth_inc_from_prev = 0
  while input_str := fp.readline():
    current_depth = int(input_str)
    if prev_depth and current_depth > prev_depth:
      depth_inc_from_prev += 1
    prev_depth = current_depth    
