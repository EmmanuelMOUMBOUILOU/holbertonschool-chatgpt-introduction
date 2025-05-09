#!/usr/bin/python3

def print_board(board):
    """Display the current game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there's a winner."""
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_full(board):
    """Check if the board is full (for draw condition)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main game loop."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input with error handling
        try:
            row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid position! Must be between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
