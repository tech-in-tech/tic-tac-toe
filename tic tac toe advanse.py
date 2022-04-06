# function to print tic tac toe board 

from lib2to3.pgen2.tokenize import TokenError
from optparse import Values
from random import choice, gammavariate
from shutil import move
from ssl import Options


def print_tic_tac_toe(values):
    print("\n")
    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print('\t     |     |')

    print('\t     |     |')
    print('\t  {}  |  {}  |  {}'.format(values[6], values[7], values[8]))
    print('\t_____|_____|_____')

# function to print scoreboard for the game
def print_scoreboard(score_board):
    print('\t-------------------------------------------')
    print('\t          SCOREDOARD TO TIC TAC TOE        ')
    print('\t-------------------------------------------')

    players = list(score_board.keys())
    print('\t  ',players[0], '\t  ', score_board[players[0]])
    print('\t  ',players[1], '\t  ', score_board[players[1]])

    print('\t------------------------------------------------------\n')


# function to check if any player wan the game
def check_winner(player_position, current_player):
    # all possible win combination of the player
    soln = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    # loop to check if any combination is satisfied or not
    for x in soln:
        if all(y in player_position[current_player] for y in x):
            # return true if any combination is satisfied in the iteration
            return True
    # return false if the above combination is not satisfied
    return False

    # function to check if the game is draw
def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O'])==9:
        return True
    return False
    # function for a single tic tac toe gamma
def single_game(current_player):

        # represent a tic tac Toe
    values=[" " for x in range(9)]

        # stores a position occupied by X and O
    player_position = {"X":[], "O":[]}

        # game loop for a single game of tic tac toe
    while True:
        print_tic_tac_toe(values)

            # try exception block for move input
        try:
            print("player ",current_player , "turn. which box? : ", end="")
            move = int(input())
        except ValueError:
            print("wrong iput!!!! try again")
            continue
            # sanity check for move input
        if move < 1 or move > 9:
            print("please chose the right number between 1 to 9")
            continue

            # check the cell is occupied or not
        if values[move-1] != " ":
            print('the place you have chosen is alredy occupied!! try again')
            continue

            # update game status 

            # updating board status   
        values[move-1]=current_player

            # updating player position
        player_position[current_player].append(move)

            # function call for cheaking winner
        if check_winner(player_position, current_player):
            print_tic_tac_toe(Values)
            print("player ",current_player, " has wan the match!!! ")
            print('\n')
            return current_player

            # function call for checking draw game
        if check_draw(player_position):
            print_tic_tac_toe(values)
            print('game is drow')
            print('\n')
            return "D"
            # switch player move
        if current_player == 'X':
            current_player == 'O'
        else:
            current_player='X'
if __name__ == "__main__":
    print("player 1 details")
    play1=input("enter the name of the player : ")
    print('\n')

    print("player 2 details ")
    play2 = input('emter the name of player 2 : ')
    print('/n')
    # stores the player who choose X and O
    current_player="play1"
    # stores the choise of players cherecter 
    player_choice = {"X":"","O":""}

    # stores the option
    optionsb = ["X","O"]

    # stores the scoreboard detailes
    score_board = {'play1': 0,'play2': 0}
    print_scoreboard(score_board)

    # game loop for a series of tic tac toe
    # the loop runs until either of the players choose to quit
    while True:

        # player choose menu
        print("turn to choose for", current_player)
        print("enter 1 for X")
        print("enter 2 for O")
        print("enter 3 for ouit")

        # try exciption for choice input
        try:
            choice=int(input())
        except ValueError:
            print("wrong input!! try again\n")
            continue

        # condition for player choice
        if choice == 1:
            player_choice["X"]=current_player
            if current_player==play1:
                player_choice['O']=play2
            else:
                player_choice['O']=play1
        elif choice==2:
            player_choice['O']=current_player
            if current_player == play1:
                player_choice['X'] = play2
            else:
                player_choice['X']=play1

        elif choice==3:
            print('final score')
            print_scoreboard(score_board)
            break
        else:
            print('wrong choice!!! try again\n')
        # stores a winner in a single game of tic tac toe
        winner=single_game(Options[choice-1])

        # scoreboard edit according to the winner
        if winner != "D":
            player_won=player_choice[winner]
            score_board[player_won]=score_board[player_won]+1

        print_scoreboard(score_board)
        # switch playerwho choose X and O
        if current_player==play1:
            current_player=play2
        else:
            current_player=play1









