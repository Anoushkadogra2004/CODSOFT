import math

# Function to print the board
def print_board(board):
    print()
    for i in range(3):
        print(board[3*i], "|", board[3*i+1], "|", board[3*i+2])
        if i < 2:
            print("---------")
    print()

# Function to check if a player has won
def check_winner(board):
    # All winning combinations
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]  # Return 'X' or 'O'

    if " " not in board:  # No spaces left → Draw
        return "Draw"

    return None  # No winner yet

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)

    # Scoring system
    if winner == "O":  # AI wins
        return 10 - depth
    elif winner == "X":  # Human wins
        return depth - 10
    elif winner == "Draw":
        return 0

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth+1, False, alpha, beta)
                board[i] = " "
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:  # Pruning
                    break
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth+1, True, alpha, beta)
                board[i] = " "
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:  # Pruning
                    break
        return best_score

# Function for AI to make a move
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)

    while True:
        # Human move
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] != " ":
            print("Invalid move. Try again.")
            continue
        board[human_move] = "X"
        print_board(board)

        if check_winner(board):
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = "O"
        print("AI plays:")
        print_board(board)

        if check_winner(board):
            break

    # Game over
    winner = check_winner(board)
    if winner == "Draw":
        print("It's a draw!")
    else:
        print(winner, "wins!")

# Start the game
play_game()