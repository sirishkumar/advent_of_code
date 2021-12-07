import numpy as np

from utils import get_lantern_fish_after_n_steps


def test_get_lantern_fish_0_days():
    in_fish = np.array([1, 2, 3, 4])
    result = get_lantern_fish_after_n_steps(in_fish, 0)

    assert np.all(result == in_fish)


def test_get_lantern_fish_1_days():
    in_fish = np.array([1, 2, 3, 4])
    result = get_lantern_fish_after_n_steps(in_fish, 1)

    assert np.all(result == np.array([0, 1, 2, 3]))


def test_get_lantern_fish_one_added_after_delivery():
    in_fish = np.array([1, 2, 3, 4])
    result = get_lantern_fish_after_n_steps(in_fish, 2)

    assert np.all(result == np.array([6, 0, 1, 2, 8]))


def test_get_lantern_fish_two_added_after_delivery():
    in_fish = np.array([1, 2, 3, 4])
    result = get_lantern_fish_after_n_steps(in_fish, 3)

    assert np.all(result == np.array([5, 6, 0, 1, 7, 8]))
