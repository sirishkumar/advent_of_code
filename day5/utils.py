from dataclasses import dataclass
from typing import List, Generator, Tuple

import numpy as np


@dataclass
class Point:
    x: int
    y: int


@dataclass
class LineSegment:
    start: Point
    end: Point


def get_line_segments(input_lines: List[str]) -> Generator[LineSegment, None, None]:
    for line in input_lines:
        points = [point.strip().split(",") for point in line.split("->")]
        start = Point(int(points[0][0]), int(points[0][1]))
        end = Point(int(points[1][0]), int(points[1][1]))
        line_segment = LineSegment(start=start, end=end)
        yield line_segment


def get_points_between(start: int, end: int) -> np.array:
    return np.linspace(start, end, abs(end - start) + 1, dtype=int)


def get_points_on_diagonal(line_segment: LineSegment) -> List[Tuple[int, int]]:
    xs = get_points_between(line_segment.start.x, line_segment.end.x)
    ys = get_points_between(line_segment.start.y, line_segment.end.y)
    return [(x, y) for x, y in zip(xs, ys)]


def get_points_on_segment(line_segment: LineSegment, include_diag: bool) -> Generator[Tuple[int, int], None, None]:
    points_on_line = []
    if line_segment.start.x == line_segment.end.x:
        points = get_points_between(line_segment.start.y, line_segment.end.y)
        for point in points:
            points_on_line.append((line_segment.start.x, point))
    elif line_segment.start.y == line_segment.end.y:
        points = get_points_between(line_segment.start.x, line_segment.end.x)
        for point in points:
            points_on_line.append((point, line_segment.start.y))
    elif include_diag and abs(line_segment.end.x - line_segment.start.x) == abs(
            line_segment.end.y - line_segment.start.y):
        points_on_line = get_points_on_diagonal(line_segment)
    return points_on_line
