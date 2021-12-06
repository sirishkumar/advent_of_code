import numpy as np

from day5.utils import get_points_between, LineSegment, Point, get_points_on_segment
from utils import get_points_on_diagonal


def test_get_points_between_1():
    result = get_points_between(4, 4)
    assert np.all(result == np.array([4]))


def test_get_points_between_2():
    result = get_points_between(4, 8)
    assert np.all(result == np.array([4, 5, 6, 7, 8]))


def test_get_points_on_segment_1():
    line_segment = LineSegment(start=Point(0, 0), end=Point(0, 0))
    points = get_points_on_segment(line_segment)
    assert points == [(0, 0)]


def test_get_points_on_segment_2():
    line_segment = LineSegment(start=Point(0, 0), end=Point(4, 0))
    points = get_points_on_segment(line_segment)
    assert points == [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]


def test_points_on_diagonal_1():
    line_segment = LineSegment(start=Point(0, 0), end=Point(3, 3))
    points = get_points_on_diagonal(line_segment)

    assert points == [(0, 0), (1, 1), (2, 2), (3, 3)]


def test_points_on_diagonal_2():
    line_segment = LineSegment(start=Point(9, 7), end=Point(7, 9))
    points = get_points_on_diagonal(line_segment)

    assert points == [(9, 7), (8, 8), (7, 9)]
