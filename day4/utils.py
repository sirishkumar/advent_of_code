from typing import List, Generator, Optional

import numpy as np

from logging_utils import print_board


class Board:
    last_drawn_number = 0

    def __init__(self, rows: List[List[int]]):
        self._board_complete = False
        self.data = np.array(rows)
        # initialize array of size self.data with false
        self.drawn_indices = np.zeros(self.data.shape, dtype=bool)

    def mark_item_selected(self, number: int) -> None:
        """Set elements in self.drawn_indices as True where number is found in self.data"""
        self.drawn_indices = np.where(self.data == number, True, self.drawn_indices)
        Board.last_drawn_number = number

    def update_board_complete_status(self) -> bool:
        """Check if all elements in a row or column in self.drawn_indices are True"""
        self._board_complete = np.any(np.all(self.drawn_indices, axis=0)) or np.any(np.all(self.drawn_indices, axis=1))
        return self.board_complete

    def get_score(self) -> int:
        """Get the score of the board"""
        return np.sum(np.where(self.drawn_indices == False, self.data, 0)) * Board.last_drawn_number

    @property
    def board_complete(self) -> bool:
        return self._board_complete


def get_drawn_numbers(line: str) -> List[int]:
    """
    Returns a list of numbers drawn from the line.
    """
    return [int(x) for x in line.split()]


def get_boards(lines: List[str]) -> Generator[Board, None, None]:
    rows = []
    for line in lines:
        row: List[int] = [int(num) for num in line.split()]
        if row:
            rows.append(row)
        else:
            board = Board(rows)
            rows = []
            yield board
    yield Board(rows)


def get_input(input_line: str) -> List[int]:
    return [int(num) for num in input_line.split(",")]


def find_first_board_to_win(boards: List[Board], drawn_numbers: List[int]) -> Optional[Board]:
    for number in drawn_numbers:
        for board in boards:
            board.mark_item_selected(number)
            if board.update_board_complete_status():
                return board


def find_last_board_to_win(boards: List[Board], drawn_numbers: List[int]) -> Optional[Board]:
    for number in drawn_numbers:
        for board in boards:
            if board.board_complete:
                continue

            board.mark_item_selected(number)
            board.update_board_complete_status()
            if board.board_complete:
                is_last_board = all(board.board_complete for board in boards)
                if is_last_board:
                    return board


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    drawn_numbers = get_input(lines[0])

    boards = []
    for board in get_boards(lines[2:]):
        boards.append(board)

    # print_live_boards(boards, drawn_numbers)

    # find the first board to win
    board = find_first_board_to_win(boards, drawn_numbers)
    print(f"First Board Score: {board.get_score()}")
    print_board(board)

    # find the last board to win
    board = find_last_board_to_win(boards, drawn_numbers)
    print(f"Last Board Score: {board.get_score()}")
    print_board(board)
