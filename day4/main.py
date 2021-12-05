from logging_utils import print_board
from utils import get_input, get_boards, find_first_board_to_win, find_last_board_to_win

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
