from copy import deepcopy
from typing import List

from src.utils import get_sum_of_cols_of_textlines_at_index


def drop_all_lines_with(textlines: List[str], index: int, val: int) -> List[str]:
    return [line for line in textlines if line[index] != str(val)]


if __name__ == "__main__":
    with open("input.txt") as f:
        data_lines_o2_rating = [line.strip() for line in f.readlines()]

    data_lines_co2_scrub_rating = deepcopy(data_lines_o2_rating)

    o2_gen_rating: List[int] = []
    co2_scrubber_rating: List[int] = []
    index = 0
    while index < len(data_lines_o2_rating[0]) and len(data_lines_o2_rating) > 1:
        count_ones_in_col_o2 = get_sum_of_cols_of_textlines_at_index(data_lines_o2_rating, index)
        if count_ones_in_col_o2 >= (len(data_lines_o2_rating) - count_ones_in_col_o2):
            data_lines_o2_rating = drop_all_lines_with(data_lines_o2_rating, index, 0)
        else:
            data_lines_o2_rating = drop_all_lines_with(data_lines_o2_rating, index, 1)

        index += 1

    index = 0
    while index < len(data_lines_co2_scrub_rating[0]) and len(data_lines_co2_scrub_rating) > 1:
        count_ones_in_col_co2 = get_sum_of_cols_of_textlines_at_index(data_lines_co2_scrub_rating, index)
        if count_ones_in_col_co2 >= (len(data_lines_co2_scrub_rating) - count_ones_in_col_co2):
            data_lines_co2_scrub_rating = drop_all_lines_with(data_lines_co2_scrub_rating, index, 1)
        else:
            data_lines_co2_scrub_rating = drop_all_lines_with(data_lines_co2_scrub_rating, index, 0)
        index += 1

    o2_gen_rating = int(data_lines_o2_rating[0], 2)
    co2_scrubber_rating = int(data_lines_co2_scrub_rating[0], 2)
    print(f"O2 gen rating: {o2_gen_rating}")
    print(f"CO2 gen rating: {co2_scrubber_rating}")
    print(f"Total rating: {o2_gen_rating * co2_scrubber_rating}")
