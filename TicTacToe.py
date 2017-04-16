

def reset_board():
    board = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"]]
    return board


def player_input():
    row = -1
    col = -1
    while row > 2 or row < 0:
        row = raw_input("Please enter the row: ")
        row = int(row)

    while col > 2 or col < 0:
        col = input("Please enter the column: ")
        col = int(col)

    return row-1, col-1

def print_board(board):
    # type: (object) -> object
    for x in xrange(0, len(board)):
        print board[x]


def place_turn(board,p):
    print "Player %s, please enter your move..." % p
    x, y = player_input()
    if board[x][y] == "-":
        board[x][y] = p
    else:
        print "Sorry, that place has already been taken."
        place_turn(board, p)


def check_game(board):
    # Check if it is a tie
    if "-" not in board[0] or "-" not in board[1] or "-" not in board[1]:
        print "It was a tie, game over!"
        return True

    # Iterate through the board
    for x in xrange(0,len(board)):
        # Test for horizontal win
        if len(set(board[x])) == 1 and (board[x][0] == "O" or board[x][0] == "X"):
            print "Player %s has won!" % board[x][0]
            return True
        # Test for vertical win
        elif len(set([board[0][x],board[1][x],board[2][x]])) == 1 and (board[0][x] == "O" or board[0][x] == "X"):
            print "Player %s has won!" % board[0][x]
            return True
        else:
            pass
    # Check the diagonals
    if board[1][1] is not "-":
        # Diagonal from top left to bottom right
        if board[0][0] == board[1][1] == board[2][2]:
            print "Player %s has won!" % board[1][1]
            return True
        # Diagonal from bottom left to top right
        elif board[0][2] == board[1][1] == board[2][0]:
            print "Player %s has won!" % board[1][1]
            return True
    return False

board = reset_board()
last_turn = ""

while not check_game(board):

    if last_turn == "" or last_turn == "O":
        place_turn(board, "X")
        last_turn = "X"

    elif last_turn == "X":
        place_turn(board, "O")
        last_turn = "O"

    print_board(board)


