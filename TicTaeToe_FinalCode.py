# Milestone Project 1
# Congratulations on making it to your first milestone!
#
# You've already learned a ton and are ready to work on a real project.
#
# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.
#
# Here are the requirements:
#
# -2 players should be able to play the game (both sitting at the same computer)
# -The board should be printed out every time a player makes a move
# -You should be able to accept input of the player position and then place a symbol on the board
#
# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!)
# Keep in mind that this project can take anywhere between several hours to several days.
#
# There are 4 Jupyter Notebooks related to this assignment:
#
# This Assignment Notebook
# -A "Walkthrough Steps Workbook" Notebook
# -A "Complete Walkthrough Solution" Notebook
# -An "Advanced Solution" Notebook
#
# I encourage you to just try to start the project on your own without referencing any of the notebooks.
# If you get stuck, check out the next lecture which is a text lecture with helpful hints and steps.
# If you're still stuck after that, then check out the Walkthrough Steps Workbook, which breaks up the project in steps for you to solve.
# Still stuck? Then check out the Complete Walkthrough Solution video for more help on approaching the project!
#
# There are parts of this that will be a struggle...and that is good! I have complete faith that if you have made it this far through the course you have all the tools and knowledge to tackle this project. Remember, it's totally open book, so take your time, do a little research, and remember:
# HAVE FUN!


#As of 11/1/2018 i make an honest attempt to do this from scratch, but after a few days I was spinning my wheels and not making any progress. So, I got help on which functions
#to create. The code in the functions and logic is all mine though.

import random

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with
# a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):
    #we need a 3x3 grid. board[] is X and O are each board position
    print(board[1] + "  |  " + board[2] + "  |  " + board[3])
    print("-----------")
    print(board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("-----------")
    print(board[7] + "  |  " + board[8] + "  |  " + board[9])



# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
def player_input():
    letter = "" #empty string

    while not(letter == "X" or letter == "O"):
        letter = input("Ok, Player 1. Do you want to be X or 0? \n").upper()

    choices = ["X", "O"] #list of our choices

    print("Player 1 has chosen " + letter)
    choices.remove(letter) #remove letter from list
    print("That means Player 2 is " + choices[0])

    #return a [X,O] or [O,X} depending on what player 1 has chosen
    if(letter == "X"):
        return ["X","O"]
    else:
        return ["O","X"]



# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker



# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    # A winner is when there are three X's or O's in a row, column, or diagonally. We need to check the make sure the at consecutive cells to see if they are equal
    #test if the values in a row are equal
    if(board[1] == mark and board[2] == mark and board[3] == mark):
        return True
    elif(board[4] == mark and board[5] == mark and board[6] == mark):
        return True
    elif(board[7] == mark and board[8] == mark and board[9] == mark):
        return True
    #test if the values in the columns are equal
    elif(board[1] == mark and board[4] == mark and board[7] == mark):
        return True
    elif(board[2] == mark and board[5] == mark and board[8] == mark):
        return True
    elif(board[3] == mark and board[6] == mark and board[9] == mark):
        return True
    #test if the values in the diagonals are equal
    elif(board[1] == mark and board[5] == mark and board[9] == mark):
        return True
    elif(board[3] == mark and board[5] == mark and board[7] == mark):
        return True
    #otherwise we don't have a winner so we return false
    else:
        return False




# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint()
# Return a string of which player went first.
def choose_first():
    whoGoesFirst = random.randint(0,10)

    if(whoGoesFirst > 5):
        return "Player 1 goes"
    else:
        return "Player 2 goes"




# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    return board[position] == ""




# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    #board is full if all of the rows and columns and contain a value. We will check to see if they are blank, not for X's  and O's
    if(board[1] != "" and board[2] != "" and board[3] != ""
            and board[4] != "" and board[5] != "" and board[6] != ""
            and board[7] != "" and board[8] != "" and board[9] != ""):
        return True
    else:
        return False


# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position.
# If it is, then return the position for later use.
def player_choice(board):
    next_position = int(input("What's is your next position: \n"))

    if(space_check(board, next_position)):
        #since true is return, we return the position number
        return next_position

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    play = input("Do you want to play again? Enter Y or N: \n")

    if(play.upper() == "Y"):
        return True
    else:
        return False



# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
print("Welcome to Tic Tac Toe! \n")

while True:
    #we need to clear the board from the last game
    working_board = [""]*10
    #we need to determine if player 1 is X or O
    #an array of two strings is return so we unpack them to the variables below
    player1, player2 = player_input()

    #we need to decide who is going first
    turn = choose_first()
    print(turn + " first\n")

    gameIsPlaying = True

    while gameIsPlaying:
        #player 1's turn
        if(turn == "Player 1 goes"):
            print("Player 1's turn \n")
            print("This is the current board: \n\n")
            display_board(working_board) #show the current board
            print("\n")
            board_position = player_choice(working_board)  #get the position you want to place your X or O
            place_marker(working_board,player1,board_position) #X or O was places at board_position

            #we just placed a X or O. We need to check if we have 3 X's or O's in a row
            if(win_check(working_board,player1)):
                #board is full and a row, column, or diagonal all equal X or O
                print("Player 1 won the game!!!! \n")
                display_board(working_board) #show the current board
                gameIsPlaying = False
                #break out of inner loop and play again
            #the game might be over if the board is full after insertion so we need to check
            else:
                if(full_board_check(working_board)):
                    #board is full and nobody won so we break out of loop and play again
                    display_board(working_board) #show the current board
                    print("The game is a tie!!!")
                    break
                else:
                    #board is not full and you don't have 3 in a row so it's player 2 turn
                    turn = "Player 2 goes"

        #player 2's turn
        else:
            print("Player 2's turn \n")
            print("This is the current board: \n\n")
            display_board(working_board) #show the current board
            board_position = player_choice(working_board)  #get the position you want to place your X or O
            print("\n")
            place_marker(working_board,player2,board_position) #X or O was places at board_position

            #we just placed a X or O. We need to check if we have 3 X's or O's in a row
            if(win_check(working_board,player2)):
                #board is full and a row, column, or diagonal all equal X or O
                print("Player 2 won the game!!!!\n")
                display_board(working_board) #show the current board
                gameIsPlaying = False
                #break out of inner loop and play again
            #the game might be over if the board is full after insertion so we need to check
            else:
                if(full_board_check(working_board)):
                    #board is full and nobody won so we break out of loop and play again
                    display_board(working_board) #show the current board
                    print("The game is a tie!!!")
                    break

                else:
                    #board is not full and you don't have 3 in a row so it's player 2 turn
                    turn = "Player 1 goes"

    if not replay(): #break out of outer loop
        break