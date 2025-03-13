import numpy as np

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = np.array([[" "] * 3 for _ in range(3)])
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-2, separated by space): ").split())
            if board[row][col] != " ":
                print("pick another cell. this one's taken!")
                continue
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"player {player} wins!")
                break
            if is_full(board):
                print_board(board)
                print("it's a tie!")
                break
            turn += 1
        except (ValueError, IndexError):
            print("invalid input")

tic_tac_toe()
