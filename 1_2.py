with open("input.txt") as fp:
  first, second, third = (None, None, None)
  prev_sum = None
  current_sum = None
  depth_increase_count = 0
  while input_str := fp.readline():
    current_input = int(input_str)
    first, second, third = (second, third, current_input)
    if first and second and third:
        current_sum = (first+second+third)

    if prev_sum and (current_sum > prev_sum):
      depth_increase_count += 1

    prev_sum = current_sum

