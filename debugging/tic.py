#!/usr/bin/python3

def print_board(board):
    """Affiche l'état actuel du plateau de jeu"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Vérifie si un joueur a gagné"""
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Vérifie la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Logique principale du jeu Tic-Tac-Toe"""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while not check_winner(board):
        print_board(board)
        valid_input = False

        # Boucle pour valider les entrées de l'utilisateur
        while not valid_input:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Vérifie si les coordonnées sont valides
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input. Row and column must be between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    valid_input = True

            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")
        
        # Si la case est vide, le joueur marque la case
        board[row][col] = player

        # Change de joueur après chaque coup
        if player == "X":
            player = "O"
        else:
            player = "X"

    print_board(board)
    # Le joueur qui a fait le dernier coup est celui qui a gagné, donc on change l'annonce du gagnant
    if player == "X":
        print("Player O wins!")
    else:
        print("Player X wins!")

# Lancer le jeu
tic_tac_toe()
