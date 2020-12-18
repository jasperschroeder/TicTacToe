import random


class TicTacToe:

    def __init__(self, board):
        self.board = board
        self.active = True
        self.openSpots = 9

    def reset_board(self):
        self.board = playingboard


def display_board(game):
    board = game.board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print('\n')


def clean_board(game):
    board = game.board
    for i in range(len(board)):
        board[i] = "-"


def drawx(game, pos):
    board = game.board
    board[pos-1] = 'X'
    game.openSpots -= 1
    display_board(game)


def drawo(game, pos):
    board = game.board
    board[pos-1] = 'O'
    game.openSpots -= 1
    display_board(game)


def check_win(game):
    board = game.board
    if game.openSpots != 0:
        if board[0] == board[1] == board[2] != "-":
            print("This is a win! " + board[0] + " won!")
            game.active = False
        elif board[3] == board[4] == board[5] != "-":
            print("This is a win! " + board[3] + " won!")
            game.active = False
        elif board[6] == board[7] == board[8] != "-":
            print("This is a win!" + board[6] + " won!")
            game.active = False
        elif board[0] == board[3] == board[6] != "-":
            print("This is a win!" + board[0] + " won!")
            game.active = False
        elif board[1] == board[4] == board[7] != "-":
            print("This is a win! " + board[1] + " won!")
            game.active = False
        elif board[2] == board[5] == board[8] != "-":
            print("This is a win! " + board[2] + " won!")
            game.active = False
        elif board[0] == board[4] == board[8] != "-":
            print("This is a win! " + board[0] + " won!")
            game.active = False
        elif board[6] == board[4] == board[2] != "-":
            print("This is a win! " + board[6] + " won!")
            game.active = False
        else:
            print("No Win yet. Keep playing!")


def check_tie(game):
    if (game.active is True) & (game.openSpots == 0):
        print("Game Over! This is a tie.")
        game.active = False


def reset_board(board):
    for i in range(len(board)):
        board[i] = "-"


def inputposition(game):
    global numpos
    while True:
        try:
            numpos = int(input())
            if (numpos < 1) | (numpos > 9):
                print("Position has to be between 1 and 9.")
            elif (game.board[numpos - 1] == 'X') | (game.board[numpos - 1] == 'O'):
                print("Position already filled!")
            else:
                break
        except TypeError:
            print("Needs to be a proper numeric value!")
        except ValueError:
            print("Needs to be a proper numeric value!")


def playing_tictactoe(game):
    print("""
    ----------------------------------------------------------------
    | Welcome to a game of TicTacToe, designed for 2 players!      |
    |                                                              |
    | In order to draw an X or an O, you have to input the number  |
    | of the square in which you want it to be drawn.              |
    | The following shows you which number refers to which square: |
    |                                                              |
    |       1 | 2 | 3                                              |
    |       4 | 5 | 6                                              |
    |       7 | 8 | 9                                              |
    |                                                              |
    | Enjoy the game!                                              |
    ----------------------------------------------------------------  
    """)
    display_board(game)
    while True:
        if random.random() > 0.5:
            while game.active is True:
                print("X's turn: Input position.")
                inputposition(game)
                drawx(game, numpos)
                check_win(game)
                if game.openSpots == 0:
                    check_tie(game)

                if game.active is True:
                    print("O's turn: Input position.")
                    inputposition(game)
                    drawo(game, numpos)
                    check_win(game)
                    if game.openSpots == 0:
                        check_tie(game)
        else:
            while game.active is True:
                print("O's turn: Input position.")
                inputposition(game)
                drawo(game, numpos)
                check_win(game)
                if game.openSpots == 0:
                    check_tie(game)

                if game.active is True:
                    print("X's turn: Input position.")
                    inputposition(game)
                    drawx(game, numpos)
                    check_win(game)
                    if game.openSpots == 0:
                        check_tie(game)

        reset_board(game.board)

        print("Do you want to start a new game?")
        print("Please type in Yes/No.")
        a = input()
        if a == "Yes":
            game.active = True
            display_board(game)
        else:
            print("Okay. Goodbye!")
            break


playingboard = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]

gameplay = TicTacToe(playingboard)
playing_tictactoe(gameplay)
