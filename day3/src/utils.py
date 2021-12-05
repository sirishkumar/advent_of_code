from typing import List, Generator


def get_input_text(file_name: str = "input.txt") -> List[str]:
    with open(file_name) as f:
        return f.readlines()


def get_entry(lines: List[str]) -> Generator[List[int], None, None]:
    """Read characters in order from every line and convert to int and add them"""

    # get each character from each line and convert to int
    for line in lines:
        yield [int(char) for char in line]


def get_sum_of_cols_of_textlines(lines: List[str]) -> List[int]:
    """Get sum of each column in text"""
    result: List[int] = [0] * len(lines[0])
    for codes in get_entry(lines):
        for i, code in enumerate(codes):
            result[i] += code
    return result


def get_sum_of_cols_of_textlines_at_index(lines: List[str], index: int) -> int:
    """Get sum of each column in text"""
    result: int = 0
    for codes in get_entry(lines):
        result += int(codes[index])
    return result
