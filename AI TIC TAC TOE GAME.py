import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']

def minimax(board, depth, maximizing_player, alpha, beta):
    if is_winner(board, 'O'):
        return -1
    elif is_winner(board, 'X'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for row, col in get_empty_cells(board):
            board[row][col] = 'X'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[row][col] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in get_empty_cells(board):
            board[row][col] = 'O'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[row][col] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_eval = float('-inf')
    best_move = None

    for row, col in get_empty_cells(board):
        board[row][col] = 'X'
        eval = minimax(board, 0, False, float('-inf'), float('inf'))
        board[row][col] = ' '

        if eval > best_eval:
            best_eval = eval
            best_move = (row, col)

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Human player's move
        row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Invalid move. Try again.")
            continue
        if is_winner(board, 'O'):
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print("AI player is making a move...")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = 'X'

        if is_winner(board, 'X'):
            print_board(board)
            print("AI player wins! Better luck next time.")
            break

if __name__ == "__main__":
    main()