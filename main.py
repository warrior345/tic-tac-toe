# Function to print tic-tac-toe
def print_tic_tac_toe(values):
    print("\n")

    print("\t      |      |")
    print("\t   {}  |   {}  |   {}".format(values[0], values[1], values[2]))
    print("\t______|______|______")

    print("\t      |      |")
    print("\t   {}  |   {}  |   {}".format(values[3], values[4], values[5]))
    print("\t______|______|______")

    print("\t      |      |")
    print("\t   {}  |   {}  |   {}".format(values[6], values[7], values[8]))
    print("\t      |      |")

    print("\n")


# print scoreboard
def print_scoreboard(score_board):
    print("\t------------------------------------")
    print("\t\t\t\tSCOREBOARD")
    print("\t------------------------------------")
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
    print("\t------------------------------------")


# Function to check win.
def check_win(player_pos, cur_player):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            return True
    return False


# Function to check draw.
def draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


# Function for a single game of tic-tac-toe
def single_game(cur_player):
    # Represents the tic-tac-toe
    values = [' ' for _ in range(9)]

    # Store the positions occupied by 'X' and 'O'
    player_pos = {'X': [], 'O': []}

    # Game loop
    while True:
        print_tic_tac_toe(values)
        try:
            print(f"Player {cur_player} turn. Which box?: ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input. Please Try Again.")
            continue

        if move < 1 or move > 9:
            print("Wrong Input! Try Again.")
            continue

        if values[move - 1] != ' ':
            print("Already occupied block. Try Again.")
            continue

        values[move - 1] = cur_player
        player_pos[cur_player].append(move)

        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print(f"Player {cur_player} has won the game.")
            return cur_player

        if draw(player_pos):
            print_tic_tac_toe(values)
            print("Match Draw.")
            return 'D'

        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


if __name__ == "__main__":
    # Ascii Character
    print('''
    
    ___________.__               ___________                     ___________            
    \__    ___/|__| ____         \__    ___/____    ____         \__    ___/___   ____  
      |    |   |  |/ ___\   ______ |    |  \__  \ _/ ___\   ______ |    | /  _ \_/ __ \ 
      |    |   |  \  \___  /_____/ |    |   / __ \\  \___  /_____/ |    |(  <_> )  ___/ 
      |____|   |__|\___  >         |____|  (____  /\___  >         |____| \____/ \___  >
                       \/                       \/     \/                            \/ 
                                                                                                        
    ''')

    print("Player 1")
    player_1_name = input("Enter the name: ")
    print("\n")
    print("Player 2")
    player_2_name = input("Enter the name: ")
    print("\n")

    cur_player_name = player_1_name
    player_choice = {'X': '', 'O': ''}
    options = ['X', 'O']
    score_board = {player_1_name: 0, player_2_name: 0}
    print_scoreboard(score_board)

    count = 0

    while True:
        print("\n")
        print(f"Time to choose for {cur_player_name}:\n")
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 for quit.  ", end="")

        try:
            choice = int(input())
            print("\n")
        except ValueError:
            print("Wrong Input. Try Again.")
            continue

        if choice == 1:
            count += 1
            print(count)
            player_choice['X'] = cur_player_name
            if cur_player_name == player_1_name:
                player_choice['O'] = player_2_name
            else:
                player_choice['O'] = player_1_name

        elif choice == 2:
            count += 1
            print(count)
            player_choice['O'] = cur_player_name
            if cur_player_name == player_1_name:
                player_choice['X'] = player_2_name
            else:
                player_choice['X'] = player_1_name

        elif choice == 3:
            print("\nFinal Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wrong choice. Try Again.")
            continue

        winner = single_game(options[choice - 1])

        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] += 1

        print_scoreboard(score_board)

        if cur_player_name == player_1_name:
            cur_player_name = player_2_name
        else:
            cur_player_name = player_1_name
