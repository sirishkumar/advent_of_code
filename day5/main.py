import collections

from utils import get_points_on_segment, get_line_segments

if __name__ == "__main__":
    points_on_segments = []
    with open("input.txt") as f:
        input_lines = [line.strip() for line in f]
        for line_segment in get_line_segments(input_lines):
            points_on_segments.extend(get_points_on_segment(line_segment, include_diag=False))

    unique_point_count = collections.Counter(points_on_segments)
    num_occurances_count = collections.Counter(unique_point_count.values())
    print(
        f"5.1 Number of points with more than 2 intersections: {sum([v for k, v in num_occurances_count.items() if k > 1])}")

    ###########################
    # Part 2
    points_on_segments = []
    with open("input.txt") as f:
        input_lines = [line.strip() for line in f]
        for line_segment in get_line_segments(input_lines):
            points_on_segments.extend(get_points_on_segment(line_segment, include_diag=True))

    unique_point_count = collections.Counter(points_on_segments)
    num_occurances_count = collections.Counter(unique_point_count.values())
    print(
        f"5.1 Number of points with more than 2 intersections: {sum([v for k, v in num_occurances_count.items() if k > 1])}")
