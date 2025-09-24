"""
A Python module for the Gomoku game.
board game where players compete to get 5 in a row
"""

from copy import deepcopy 

def newGame(player1, player2):
    """
This function returns the game dictionary

Inputs : player1,player2 must be strings
Returns : game dictionary consisting of 4 keys ; 'player1' and 'player2' are assigned the input strings.'who' is an integer value 1, and 'board' is a list of 8 lists consisting of 8 0's , an empty game board.
 
"""
    game = {
        'player1' : player1,
        'player2' : player2,
        'who' : 1,
        'board' : [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    }
    # TODO: Initialize dictionary for a new game 
    return game


# TODO: All the other functions of Tasks 2-11 go here.
def printBoard(board):
    """
    This function prints the game board

    Input: board value from game dictionary , type : list of lists
    output: prints a game board with letters above it for added readability type: string
    """
    print("A  B  C  D  E  F  G  H")
    for row in board:
        for column in row:
            print(column, end="  ")
        print("")

def posToIndex(s):
    """
    this function converts a position to index form

    input: string 's' which would be a players desired game move
    returns  : index corresponding to the players input in tuple form
    raised exceptions: ValueError will be raised if the number number or letter
                       in the input is greater than 8 or a letter after H

    """
    for ch in s:
        if ch.isnumeric() == False:
            x = ord(ch.upper())-ord('A')
        if ch.isnumeric() == True:
            y = ord(ch.upper())-ord('1')
    if x<=14:
        if y<=14:
            return (y,x)
        else:
            raise ValueError()
    else:
        raise ValueError()


def indexToPos(t):
    """
    this function converts an index to a game board position
    input: index as a tuple 't' in the form (r.c)
    returns: position corresponding to input 't' as a string
    """ 
    num = int(t[0]) + 1
    letter = chr(int(t[1]) + (ord('a')))
    return(str(num)+str(letter))   


def divide_chunks(l, n):
    """
    a funtion to divide a list into equal chunks
    inputs: l:a list , n: an integer (function divides l into n lists)
    yields: new list of lists
    """   
    for i in range(0, len(l), n):
        yield l[i:i + n]
       

def loadGame(filename):
    """this function loads a game by reading a contents from a text file
input: file name as a string : e.g 'filename.txt'
returns: game dictionary, 'player1' and 'player2' are lines 1 and 2 converted to strings respectively
'who' is line 3. 'board' is lines 4 to 11 provided that they are in the correct format
raised exceptions: raises FileNotFound error if the file cannot be loaded
raises ValueError if format of txt file is incorrect  """
    file = open(filename,'r')
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    board = []
    board2 = []
    list_1 = [modified[3]]
    list_2 = [modified[4]]
    list_3 = [modified[5]]
    list_4 = [modified[6]]
    list_5 = [modified[7]]
    list_6 = [modified[8]]
    list_7 = [modified[9]]
    list_8 = [modified[10]]
    board.append(list_1)
    board.append(list_2)
    board.append(list_3)
    board.append(list_4)
    board.append(list_5)
    board.append(list_6)
    board.append(list_7)
    board.append(list_8)
    for e in board:
        for x in e:
            for sub_e in x.split(","):
                board2.append(int(sub_e))
    x = list(divide_chunks(board2, 8))
    game = {
        'player1' : str(modified[0]),
        'player2' : str(modified[1]),
        'who' : str(modified[2]),
        'board' : x,
        }
    return game
        
    

def getValidMoves(board):
   """
   this function creates a list of all current valid moves
   input: board , a list of lists
   output: list of tuples which are indexes of all valid moves
   """ 
   valid_moves = []
   for x in board:
       for n,element in enumerate(x):
           if element == 0:
               valid_moves.append((board.index(x),n))
   return valid_moves

   
def makeMove(board,move,who):
    """
    this function replaces a 0 on the board with a 1 or 2 depending on the value of 'who'
    inputs: board: a list of lists . move: a tuple of form (r,c) . who: an integer which will be either a 1 or 2
    returns: board: a list of lists , has now been updated with a new value 

    """
    x = posToIndex(move)
    list1 = list(x)
    if who == 1:
        if board[list1[0]][list1[1]] == 0:
            board[list1[0]][list1[1]] = 1
        else:
            print("enter another value")
    elif who == 2:
        if board[list1[0]][list1[1]] == 0:
            board[list1[0]][list1[1]] = 2
    elif who != 1 != 2:
        raise ValueError("value of who must be a 1 or 2")
    return board


def hasWon(board,who):   # check all posibilities work for this one
    """
    this function checks to see if a player has won the game
    input: board: a list of lists, who: an integer
    returns: true if game has been won , or false otherwise
    """

    boardHeight = len(board)
    boardWidth = len(board[0])
    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == who and board[x+1][y] == who and board[x+2][y] == who and board[x+3][y] == who and board[x+4][y] == who:
                return True

    # win checking vertically
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == who and board[x][y+1] == who and board[x][y+2] == who and board[x][y+3] == who and board[x][y+4] == who:
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == who and board[x+1][y-1] == who and board[x+2][y-2] == who and board[x+3][y-3] == who and board[x+4][y-4] == who:
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == who and board[x+1][y+1] == who and board[x+2][y+2] == who and board[x+3][y+3] == who and board[x+4][y+4] == who:
                return True

    return False


def suggestMove1(board,who):
    """
    function suggests a move to make depending on the state of the current game board
    first suggests a winning move , if not possible , suggests a move to block an opponents winning move,
    if still not possible suggests a valid move
    inputs: board: a list of lists representing a game board
            who : an integer
    returns: a tuple of the form (r,c) representing the index of the suggested move
    """
    suggested_move = []
    suggested_win = []
    board2 = deepcopy(board)
    board3 = deepcopy(board)
    boardHeight = len(board)
    boardWidth = len(board[0])
    
    for x in range(boardHeight): # these for loops suggest moves to make to block a winning move from player 1
        for y in range(boardWidth - 3): 
           if board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3] != 0 != who:
               if board[x][y+4] == 0:
                   board2[x][y+4] = 3
               elif board[x][y-1] == 0:
                   board2[x][y-1] = 3
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
           if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y] != 0 != who:
               if board[x+4][y] == 0:
                   board2[x+4][y] = 3
               elif board[x-1][y] == 0:
                   board2[x-1][y] = 3
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
           if board[x][y] == board[x+1][y-1] == board[x+2][y-2] == board[x+3][y-3] != 0 != who:
               if board[x-1][y+1] == 0:
                   board2[x-1][x+1] = 3
               elif board[x+4][y-4] == 0:
                   board2[x+4][y-4] = 3
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
           if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] != 0 != who :
               if board[x-1][y-1] == 0:
                   board2[x-1][y-1] = 3
               elif board[x+4][y+4] == 0:
                    board2[x+4][y+4] = 3
    for x in board2:
        for n,element in enumerate(x):
            if element == 3:
                suggested_move.append((board2.index(x),n))
    
    for x in range(boardHeight): # these for loops suggest moves to make a winning move
        for y in range(boardWidth - 3): 
           if board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3] == who:
               if board[x][y+4] == 0:
                   board3[x][y+4] = 4
               elif board[x][y-1] == 0:
                   board3[x][y-1] = 4
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
           if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y] == who:
               if board[x+4][y] == 0:
                   board3[x+4][y] = 4
               elif board[x-1][y] == 0:
                   board3[x-1][y] = 4
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
           if board[x][y] == board[x+1][y-1] == board[x+2][y-2] == board[x+3][y-3] == who:
               if board[x-1][y+1] == 0:
                   board3[x-1][x+1] = 4
               elif board[x+4][y-4] == 0:
                   board3[x+4][y-4] = 4
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
           if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] == who:
               if board[x-1][y-1] == 0:
                   board3[x-1][y-1] = 4
               elif board[x+4][y+4] == 0:
                    board3[x+4][y+4] = 4
    for x in board3:
        for n,element in enumerate(x):
            if element == 4:
                suggested_win.append((board3.index(x),n))
    
    suggested = []
    valid_moves = []
    suggested.append(suggested_win)
    suggested.append(suggested_move)
    if len(suggested[0]) >= 1:
        return suggested[0][0]
    if len(suggested[0]) < 1:
        if len(suggested[1]) >= 1:
            return suggested[1][0]
        elif len(suggested[1]) < 1:
            for x in board:
                for n,element in enumerate(x):
                    if element == 0:
                        valid_moves.append((board.index(x),n))
                        return valid_moves[0]

 
# USE EXACTLY THE PROVIDED FUNCTION NAMES AND VARIABLES!

# ------------------- Main function --------------------
def play():
    """
    this function controls the game flow: has no arguments
    inputs: 'player1' and 'player2' are strings , if 'player1' is 'L' load game
    function is called , or if 'c' is entered the corresponding player will be 
    controlled by the computer
    .
    move is another string input that represents the players desired move
    outputs: prints the new game board after a board , and win/lose/draw messages
    accordingly 
    """
    
    print("*"*55)
    print("***"+" "*11+"WELCOME TO FAHEEM'S GOMOKU!"+" "*11+"***")
    print("*"*55,"\n")
    print("Enter Player 1's Name:")
    updatedDict = {'player1': input().capitalize()}
    if updatedDict['player1'] == 'L':
        print("enter the name of the file you wish to load:")
        filename = input()
        if len(filename) == 0:
                filename = 'game.txt'
        game = loadGame(filename)
    else:
        game = newGame('a', 'b')
        print("Enter Player 2's Name:")
        updatedDict2 = {'player2': input().capitalize()}
        game.update(updatedDict)
        game.update(updatedDict2)   
    printBoard(game['board'])
    while hasWon(game['board'], 1) == hasWon(game['board'], 2) == False:
        if game['player1'] == 'C':
            print("the computer1 will now make a move")
            makeMove(game['board'],indexToPos(suggestMove1(game['board'], 1)),1)
            printBoard(game['board'])  
            if hasWon(game['board'], 1) == True:
                print("Computer1 has won the game!")
                break
        else:
            print(game['player1'] + " input a move:")
            x = input()
            makeMove(game['board'], x, 1)
            printBoard(game['board'])
            if hasWon(game['board'], 1) == True:
                print(game['player1']+" has won the game!")
                break
            
        if game['player2'] == 'C':
            print("the computer2 will now make a move")
            makeMove(game['board'],indexToPos(suggestMove1(game['board'], 2)),2)
            printBoard(game['board'])  
            if hasWon(game['board'], 2) == True:
                print("Computer2 has won the game!")
                break     
        else:
            print(game['player2'] + " input a move:")
            x = input()
            makeMove(game['board'], x, 2)
            printBoard(game['board'])   
            if hasWon(game['board'], 2) == True:
                print(game['player2']+" has won the game!")
                break
            
        if len(getValidMoves(game['board'])) == 0:
            print("the game has ended in a draw")
            break
                        
                        
                        
                        
              
    print("***"+" "*11+"THANK YOU FOR PLAYING"+" "*11+"***")
    
    

    
# the following allows your module to be run as a program 

if __name__ == '__main__' or __name__ == 'builtins':
   play()



