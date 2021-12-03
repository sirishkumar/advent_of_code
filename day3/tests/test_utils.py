from src.utils import get_sum_of_cols_of_textlines


def test_sum_of_first_digits():
    input_txt = "1100\n1111"
    results = get_sum_of_cols_of_textlines(input_txt)
    assert results == [2, 2, 1, 1]
