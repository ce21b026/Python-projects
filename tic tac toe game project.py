# Tic Tac Toe

# Global variables
board = [' '] * 10
game_active = True
current_player = 'X'


# Function to display the game board
def display_board():
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-----------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")


# Function to check if any player has won
def check_win(player):
    return (
        (board[7] == board[8] == board[9] == player) or
        (board[4] == board[5] == board[6] == player) or
        (board[1] == board[2] == board[3] == player) or
        (board[7] == board[4] == board[1] == player) or
        (board[8] == board[5] == board[2] == player) or
        (board[9] == board[6] == board[3] == player) or
        (board[7] == board[5] == board[3] == player) or
        (board[9] == board[5] == board[1] == player)
    )


# Function to check if the board is full
def check_draw():
    return ' ' not in board[1:]


# Function to handle a player's turn
def handle_turn(player):
    position = input("Player " + player + ", choose a position (1-9): ")

    while True:
        if position.isdigit() and 1 <= int(position) <= 9 and board[int(position)] == ' ':
            break
        else:
            position = input("Invalid position. Player " + player + ", choose a valid position (1-9): ")

    board[int(position)] = player
    display_board()


# Function to switch players
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

# Function to reset the game
def reset_game():
    global board, game_active, current_player
    board = [' '] * 10
    game_active = True
    current_player = 'X'


# Main game loop
def play_game():
    display_board()
    game_active=True

    while game_active:
        handle_turn(current_player)

        if check_win(current_player):
            print("Player " + current_player + " wins!")
            game_active=False
        elif check_draw():
            print("It's a draw!")
            game_active=False
        else:
            switch_player()

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        reset_game()
        play_game()
    else:
        print("Thank you for playing!")


# Start the game
play_game()
