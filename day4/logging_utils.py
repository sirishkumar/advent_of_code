from typing import List

from rich.columns import Columns
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text


def print_boards(boards: List["Board"]):
    tables = []
    for board in boards:
        table = Table(show_header=False, header_style="bold magenta")
        for data_row, flags_row in zip(board.data, board.drawn_indices):
            row = []
            for x, f in zip(data_row, flags_row):
                label = Text(str(x), style="magenta")
                if f:
                    label.stylize("white on dark_red")
                else:
                    label.stylize("blue")
                row.append(label)
            table.add_row(*row)
        tables.append(table)

    return tables


def print_board(board: "Board"):
    table = Table(show_header=False, header_style="bold magenta")
    for data_row, flags_row in zip(board.data, board.drawn_indices):
        row = []
        for x, f in zip(data_row, flags_row):
            label = Text(str(x), style="magenta")
            if f:
                label.stylize("white on dark_red")
            else:
                label.stylize("blue")
            row.append(label)
        table.add_row(*row)
    console = Console()
    console.print(table)


def print_live_boards(boards: List["Board"], drawn_numbers: List[int]):
    console = Console()
    with Live(console=console) as live:
        for number in drawn_numbers:
            for board in boards:
                board.mark_item_selected(number)
            tables = print_boards(boards)
            columns = Columns(tables, padding=1, expand=True)
            console.print(columns)
