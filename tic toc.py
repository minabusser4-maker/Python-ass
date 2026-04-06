def print_board(board):
    """
    Function to display the board.
    """
    print("\n")
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print("\n")


def check_winner(board, player):
    """
    Function to check if a player has won.
    """
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    
    return False


def tic_tac_toe():
    """
    Main function to run the game.
    """
    board = ["1","2","3","4","5","6","7","8","9"]
    current_player = "X"
    
    for turn in range(9):
        print_board(board)
        
        move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        
        if board[move] in ["X", "O"]:
            print("Position already taken! Try again.")
            continue
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"
    
    print_board(board)
    print("It's a draw!")


# Run the game
tic_tac_toe()
