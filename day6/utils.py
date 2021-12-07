from collections import Counter
from typing import List

import numpy as np
from rich import print


def get_input(file: str) -> np.array:
    with open(file) as fp:
        input_str = fp.readline()
    return np.array(list(map(int, input_str.strip().split(","))))


def get_input_list(file: str) -> List[int]:
    with open(file) as fp:
        input_str = fp.readline()
    return list(map(int, input_str.strip().split(",")))


def get_lantern_fish_after_n_steps(input_lantern_fish: np.array, n: int) -> np.array:
    """
    Get the lantern fish after n steps.
    :param input_lantern_fish: list of lantern fishes and their maturity period
    :param n: number of days to run the simulation
    :return: Final lantern fish after n steps

    >>> get_lantern_fish_after_n_steps(np.array([0, 2, 7, 0]), 10)

    This solution goes out of memory for large n.
    """
    for _ in range(n):
        input_lantern_fish -= 1
        num_fish_delivered = np.sum(input_lantern_fish < 0)
        if num_fish_delivered > 0:
            input_lantern_fish[input_lantern_fish < 0] = 6
            input_lantern_fish = np.append(input_lantern_fish, np.ones(num_fish_delivered) * 8)
    return input_lantern_fish


def get_num_lantern_fish_after_n_days(input_lantern_fish: List[int], n: int) -> int:
    """
    Get the number of lantern fish after n days.
    :param input_lantern_fish: list of lantern fishes and their maturity period
    :param n: number of days to run the simulation
    :return: Final number of lantern fish after n days
    # copied from https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnm8dqm/?utm_source=share&utm_medium=web2x&context=3

    >>> get_num_lantern_fish_after_n_days(get_input_list("test_input.txt"), 18)
    26
    """
    input_counter = Counter(input_lantern_fish)
    final = Counter(dict().fromkeys(range(9), 0))
    final.update(input_counter)

    for _ in range(n):
        curr = final[0]
        for i in range(1, 9):
            final[i - 1] = final[i]
        final[6] += curr  # Number of lantern fish with maturity 6 are incremented
        final[8] = curr  # New lantern fish with maturity 8

    return sum(final.values())


if __name__ == "__main__":
    print(get_num_lantern_fish_after_n_days(get_input("input.txt"), 80))
    print(get_num_lantern_fish_after_n_days(get_input("input.txt"), 256))
    # print("Number of lantern fish after 80 days", get_lantern_fish_after_n_steps(get_input("input.txt"), 80).shape[0])
    # print("Number of lantern fish after 256 days", get_lantern_fish_after_n_steps(get_input("input.txt"), 256).shape[0])
