"""""
This is a game
9/23/2021
Jackson T

hnfhghjfjhg
"""""






print ("Welcome to Tik Tac Toe")

import random
computer_choice = ""
player_choice = ""

#this is the board to the array
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
win_x = [["x","x","x"],["x","x","x"],["x","x","x"]]
win_o = [["o","o","o"],["o","o","o"],["o","o","o"]]
def print_board():
    print("COl   0    1    2")
    print("Row 0",board[0])
    print("Row 1", board[1])
    print("Row 2", board[2])

    print_board()
  #do error handling here.
def Player_choosing():
    global player_choice
    global computer_choice
    player_choice = input("Would you like to be x or o?")
    print("greta, you ", player_choice)


    if (player_choice != "o") and (player_choice != "x"):
        print("big stinky uh oh.")
        Player_choosing()

    if player_choice == "x":
        computer_choice = "o"
        print("computer is ", computer_choice)
    if player_choice == "o":
        computer_choice = "x"
        print("computer is ", computer_choice)


def computer_moves ():
    ran_choice_row = random.randint(0,2)
    ran_choice_col = random.randint(0,2)

    if board[ran_choice_row][ran_choice_col] == " ":
        board[ran_choice_row][ran_choice_col] = computer_choice
        print_board()


    else:
        computer_moves()








def user_move ():
    user_choice_row = input("What row would you like?")
    user_choice_col = input("What collum would you like?")
    int_user_choice_row = int(user_choice_row)
    int_user_choice_col = int(user_choice_col)
    #board[int_user_choice_row][int_user_choice_col] = player_choice

    if board[int_user_choice_row][int_user_choice_col] == " " :
        board[int_user_choice_row][int_user_choice_col] = player_choice
        print_board()
    else:

        print("PICK AGAIN")
        user_move()





def gameplay():
    computer_moves()
    user_move()
    computer_moves()
    user_move()
    computer_moves()
    user_move()
    computer_moves()
    user_move()
    computer_moves()
    print()

    while True:
        if win_x[0] == board[0]:
            print("X Wins")
            break
        if win_x[0] == board[1]:
            print("X Wins")
            break
        if win_x[0] == board[2]:
            print("X Wins")
            break
        if win_x[1] == board[0]:
            print("X Wins")
            break
        if win_x[1] == board[1]:
            print("X Wins")
            break
        if win_x[1] == board[2]:
            print("X Wins")
            break
        if win_x[2] == board[0]:
            print("X Wins")
            break
        if win_x[2] == board[1]:
            print("X Wins")
            break
        if win_x[2] == board[2]:
            print("X Wins")
            break
        if win_x[2] == board[3]:
            print("X Wins")
            break
        if win_o[0] == board[0]:
            print("o Wins")
            break
        if win_o[0] == board[1]:
            print("o Wins")
            break
        if win_o[0] == board[2]:
            print("o Wins")
            break
        if win_o[1] == board[0]:
            print("o Wins")
            break
        if win_o[1] == board[1]:
            print("o Wins")
            break
        if win_o[1] == board[2]:
            print("o Wins")
            break
        if win_o[2] == board[0]:
            print("o Wins")
            break

        if win_o[2] == board[1]:
            print("o Wins")
            break
        if win_o[2] == board[2]:
            print("o Wins")
            break
        if win_o[2] == board[3]:
            print("o Wins")
            break
            #Diaganal
        if (board[0][0] == "x") and (board[1][1] == "x") and (board[2][2] == "x"):
            print ("X wins")
            break
        if (board[2][0] == "x") and (board[1][1] == "x") and (board[0][2] == "x"):
            print ("X wins")
            break
        if (board[0][0] == "o") and (board[1][1] == "o") and (board[2][2] == "o"):
            print ("o wins")
            break
        if (board[2][0] == "o") and (board[1][1] == "o") and (board[0][2] == "o"):
            print ("o wins")



       # if (board[1][0] == "x") and (board[1][1] == "x") and (board[1][2] == "x"):
          #  print ("X wins")








gameplay()















'''''
print("       I  I")
print("       I  I")
print(" ------I--I------  ")
print("       I  I")
print(" ------I--I------")
print("       I  I")
print("       I  I")
'''

Array_tik = ["       I  I","       I  I"," ------I--I------  ","       I  I"," ------I--I------","       I  I","       I  I"]

