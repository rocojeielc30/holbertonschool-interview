#!/usr/bin/python3
"""Solves the N queens puzzle and prints every solution."""
import sys


MINIMUM_BOARD_SIZE = 4


# ---------- Reading and checking the input ----------

def exit_with_message(message):
    """Print an error message and stop the program with status 1."""
    print(message)
    sys.exit(1)


def get_board_size():
    """Read N from the command line and make sure it is valid."""
    # the script name counts as one argument, so we expect exactly two
    if len(sys.argv) != 2:
        exit_with_message("Usage: nqueens N")

    user_input = sys.argv[1]

    # int() raises ValueError if the text is not a whole number
    try:
        board_size = int(user_input)
    except ValueError:
        exit_with_message("N must be a number")

    if board_size < MINIMUM_BOARD_SIZE:
        exit_with_message("N must be at least 4")

    return board_size


# ---------- Checking if a square is safe ----------

def is_same_column(queen_column, new_column):
    """Return True if both squares are in the same column."""
    return queen_column == new_column


def is_same_diagonal(queen_row, queen_column, new_row, new_column):
    """Return True if both squares are on the same diagonal."""
    # on a diagonal, you move the same distance across as you move down
    row_distance = abs(queen_row - new_row)
    column_distance = abs(queen_column - new_column)
    return row_distance == column_distance


def is_safe(placed_queens, new_row, new_column):
    """Return True if no placed queen can attack the new square."""
    # rows never clash, because we only ever place one queen per row
    for queen in placed_queens:
        queen_row = queen[0]
        queen_column = queen[1]

        if is_same_column(queen_column, new_column):
            return False

        if is_same_diagonal(queen_row, queen_column, new_row, new_column):
            return False

    # no queen was able to attack this square
    return True


# ---------- Solving the puzzle ----------

def place_queens(board_size, current_row, placed_queens):
    """Place one queen per row, printing every complete solution."""
    # base case: every row has a queen, so this is a full solution
    all_rows_filled = current_row == board_size
    if all_rows_filled:
        print(placed_queens)
        return

    # recursive step: try putting a queen in each column of this row
    for column in range(board_size):

        if not is_safe(placed_queens, current_row, column):
            continue  # this square is attacked, try the next column

        # place the queen on this square
        placed_queens.append([current_row, column])

        # solve the rest of the board starting from the next row
        next_row = current_row + 1
        place_queens(board_size, next_row, placed_queens)

        # backtrack: remove the queen so the next column can be tried
        placed_queens.pop()


def main():
    """Read N, then print every way to place N queens safely."""
    board_size = get_board_size()

    starting_row = 0
    empty_board = []
    place_queens(board_size, starting_row, empty_board)


if __name__ == "__main__":
    main()