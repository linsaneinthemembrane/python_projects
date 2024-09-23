import numpy as np

empty_board = np.array([["A1", "B1", "C1"],
                       ["A2", "B2", "C2"],
                       ["A3", "B3", "C3"]])

valid_list = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
winner = False
x_or_o: list[str] = [" X", " O"]
x_or_o_idx = 0

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def check_win(board):
    # Check rows
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2]:
            return True

    # Check columns
    for i in range(3):
        if board[0, i] == board[1, i] == board[2, i]:
            return True

    # Check diagonals
    if board[0, 0] == board[1, 1] == board[2, 2]:
        return True
    if board[0, 2] == board[1, 1] == board[2, 0]:
        return True

    return False

def check_tie(board):
    # Check if all positions are filled with " X" or " O"
    for row in board:
        for cell in row:
            if cell not in x_or_o:
                return False
    return True

while winner == False:
    print_board(empty_board)
    position = input(f"Player {x_or_o[x_or_o_idx % 2]}, choose a position: ")
    if position not in valid_list:
        print("Please enter a valid position.")
        continue
    index = valid_list.index(position)
    row = index // 3  # get the row
    col = index % 3   # get the column

# Check if the position is already taken
    if empty_board[row][col] in x_or_o:
        print("Position already taken, please choose another.")
        continue

    empty_board[row, col] = x_or_o[x_or_o_idx % 2]

    if check_win(empty_board):
        print_board(empty_board)
        print(f"Player {x_or_o[x_or_o_idx % 2]} wins!")
        winner = True
    elif check_tie(empty_board):
        print_board(empty_board)
        print("The game is a tie!")
        winner = True
    x_or_o_idx += 1


