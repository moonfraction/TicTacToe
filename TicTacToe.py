def sum(a, b, c):
    return a + b + c

def print_board(x_moves, o_moves):
    """
    Prints the Tic Tac Toe board with 'X' and 'O' moves.

    Parameters:
        x_moves (list): List representing 'X' moves on the board.
        o_moves (list): List representing 'O' moves on the board.
    """
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            symbol = 'X' if x_moves[index] else ('O' if o_moves[index] else index)
            print(symbol, end=" | " if j < 2 else "\n")
        print("--|---|--" if i < 2 else "")


def check_win(x_moves, o_moves):
    """
    Checks if there is a winner in the current game.

    Parameters:
        x_moves (list): List representing 'X' moves on the board.
        o_moves (list): List representing 'O' moves on the board.

    Returns:
        str or None: Returns 'X' or 'O' if there is a winner, None otherwise.
    """
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in win_combinations:
        if sum(x_moves[win[0]], x_moves[win[1]], x_moves[win[2]]) == 3:
            return "X"
        if sum(o_moves[win[0]], o_moves[win[1]], o_moves[win[2]]) == 3:
            return "O"
    return None


if __name__ == "__main__":
    x_moves = [0] * 9
    o_moves = [0] * 9
    current_player = 1  # 1 for X and 0 for O
    cnt = 0
    print("Welcome to Tic Tac Toe")
    
    while cnt < 9:
        print_board(x_moves, o_moves)
        
        # Determine the current player's symbol
        player_symbol = 'X' if current_player == 1 else 'O'
        print(f"{player_symbol}'s Chance")
        
        # Get user input for the move
        value = int(input("Please enter a value: "))
        
        # Input validation
        if 0 <= value <= 8 and x_moves[value] == o_moves[value] == 0:
            if current_player == 1:
                x_moves[value] = 1
            else:
                o_moves[value] = 1
            cnt += 1
        else:
            print("Invalid move. Try again.")
            continue
        
            
        # Check for a winner
        winner = check_win(x_moves, o_moves)
        if winner:
            print(f"{winner} won the match")
            break

        # Check if the game is over
        if cnt == 9:
            print("It's a draw! MATCH OVER")
            break

        # Switch player for the next turn
        current_player = 1 - current_player
