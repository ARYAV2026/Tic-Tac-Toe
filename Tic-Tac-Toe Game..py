def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(board, player):

    # Check rows
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True

    # Check columns
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
        # Check diagonals
    if board[0] == board[4] == board[8] == player:
            return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False
def check_draw(board):

    return all(cell in ['X', 'O'] for cell in board)

def play_game():

    # Initialize board with numbers 1 to 9
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'

    while True:
        print_board(board)

        # Display whose turn it is
        player_num = 1 if current_player == 'X' else 2
        print(f"Player {player_num}'s turn ({current_player})")

        move = input("Choose a position (1-9): ")

        # Input Validation using try
        try:
            position = int(move) - 1
        except ValueError:
            print("\n[Error] Invalid input. Please enter a number between 1 and 9.")
            continue

        # Input Validation: Check if number is out of range
        if position < 0 or position > 8:
            print("\n[Error] Out of range! Please choose a number between 1 and 9.")
            continue

        # Input Validation: Check if cell is already occupied
        if board[position] in ['X', 'O']:
            print("\n[Error] That cell is already occupied! Choose an empty cell.")
            continue

        # Place the player's mark
        board[position] = current_player

        # Win Detection
        if check_win(board, current_player):
            print_board(board)
            print(f" Congratulations! Player {player_num} ({current_player}) wins the game!")
            break

        # Draw Detection
        if check_draw(board):
            print_board(board)
            print("It's a draw! The board is full.")
            break

        # Switch player turns
        current_player = 'O' if current_player == 'X' else 'X'

def main():

    print("========================================")
    print("      Welcome to  Tic-Tac-Toe    ")
    print("========================================")


    while True:
        play_game()

        # Play Again Option
        choice = input("\nDo you want to play another round? (y/n): ")
        if choice != 'y' and choice != 'Y':
            print("\nThanks for playing!")
            break
    # print("\n" + "=" * 40 + "\nStarting a new round...\n" + "=" * 40)

if __name__ == "__main__":
    main()