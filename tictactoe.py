import numpy as np

# Starts the game by asking the user if they want to play
def start_game():
    user_in = input("Are you ready to play Tic Tac Toe? (Y or N): ");

    # Repeats input prompt until receives proper input
    while True:
        if user_in == "Y":
            return True
        elif user_in == "N":
            return False
        else:
            user_in = input("Please provide proper input (Y or N): ")

# Prints out game state
def print_game(game_arr):
    print("     0     1     2\n",
          "       |     |     \n",
          "0  ", game_arr[0, 0], " | ", game_arr[0, 1], " | ", game_arr[0, 2], " \n",
          "  _____|_____|_____\n",
          "       |     |     \n",
          "1  ", game_arr[1][0], " | ", game_arr[1][1], " | ", game_arr[1][2], " \n",
          "  _____|_____|_____\n",
          "       |     |     \n",
          "2  ", game_arr[2][0], " | ", game_arr[2][1], " | ", game_arr[2][2], " \n",
          "       |     |     \n")

# Determine whether player's requested spot is already taken or not
def spot_taken(row, column, game_arr):
    if game_arr[row, column] == "X" or game_arr[row, column] == "O": return 1
    else: return 0

# Changes game state according to where player places X or O
def get_player_move(player, game_arr):
    print(f"Player {player}, choose which row and column you want to select.\n")
    row = int(input("Row (0-2): "))
    column = int(input("Column (0-2): "))

    # Checks that the spot isn't already taken on the board
    if not spot_taken(row, column, game_arr):
        game_arr[row, column] = player
    else:
        print("This spot is already taken. Pick another spot.\n")
        get_player_move(player, game_arr)

    # Checks that the user gave correct coordiantes (i.e. not out of range for the 3x3 table)
    if row not in range(3) or column not in range(3):
        print("You must give valid coordinates for the board (0-2).\n")
        get_player_move(player, game_arr)

    return game_arr

# Switches the player for turns
def switch_player(player):
    if player == "X": return "O"
    else: return "X"

# Checks if a player has won
def check_for_winner(game_arr, current_player):
    # Checks for 3 straight in columns and rows
    for index in range (3):
        if game_arr[index][0] == game_arr[index][1] == game_arr[index][2] == current_player:
            return True
        if game_arr[0][index] == game_arr[1][index] == game_arr[2][index] == current_player:
            return True
    
    # Checks for 3 straight along diagonals
    if game_arr[0][0] == game_arr[1][1] == game_arr[2][2] == current_player:
        return True
    if game_arr[0][2] == game_arr[1][1] == game_arr[2][0] == current_player:
        return True

    return False

# Checks if the game has ended in a tie (i.e. if all spots have been picked)
def check_for_tie(game_arr):
    for row in range(3):
        for column in range(3):
            if game_arr[row][column] == "-": return False 

    return True

# Checks if a player has won or if there is a tie
def check_game_over(game_arr, current_player):
    return check_for_winner(game_arr, current_player) or check_for_tie(game_arr)

# Prints a message informing the user of who won
def print_winner_msg(player):
    print(f"Congrats to player {player} for winning!\n")

# Prints a message in the event the game ends in a tie
def print_tie_msg():
    print("The game has ended in a tie.\n")

# Prints either a message indicating the winner or announces a tie
def print_game_over_msg(game_arr, player):
    if check_for_winner(game_arr, player):
        print_winner_msg(player)
    else:
        print_tie_msg()

# Starts the game
def play_game():
    game_over = 0
    game_arr = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]) # Game state
    player = "O"

    print_game(game_arr)

    while not game_over: # Plays until game is over
        player = switch_player(player) # Switches player turn
        game_arr = get_player_move(player, game_arr) # Gets player's move
        print_game(game_arr) # Prints game state to console

        game_over = check_game_over(game_arr, player); # Checks if game is over

    print_game_over_msg(game_arr, player)

# Prints end game message
def end_game():
    print("Thanks for playing Tic Tac Toe today!")

# Runs game until user doesn't want to play any more
def main():
    play = start_game()

    while play:
        play_game()
        play = start_game()

    end_game();

main()