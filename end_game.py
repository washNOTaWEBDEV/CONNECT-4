import misc
from screendisplay import *
from game_board import connect4
from winning_game_line import winning_line

def end_turn(player_number, columnID):
    connect4.board[connect4.board_last_filled_up_indexes[columnID]][columnID] = player_number
    connect4.board_last_filled_up_indexes[columnID] -=1
    misc.player *= -1
    misc.turns += 1
    return


def check_gameover():
    board = connect4.board

    # rows
    for rowID, row in enumerate(board):
        for i in range(4):
            if row[i] + row[i+1] + row[i+2] + row[i+3] == 4:
                misc.winner, misc.gameover, winning_line.game_line_data = 1, True, ('horizontal', rowID, i, i+3) 
                return
            elif row[i] + row[i+1] + row[i+2] + row[i+3] == -4:
                misc.winner, misc.gameover, winning_line.game_line_data = -1, True, ('horizontal', rowID, i, i+3) 
                return

    # columns
    for i in range(7):
        for j in range(3):
            if board[j][i] + board[j+1][i] + board[j+2][i] + board[j+3][i] == 4:
                misc.winner, misc.gameover, winning_line.game_line_data = 1, True, ('vertical', i, j, j+3)
                return
            elif board[j][i] + board[j+1][i] + board[j+2][i] + board[j+3][i] == -4:
                misc.winner, misc.gameover, winning_line.game_line_data = -1, True, ('vertical', i, j, j+3)
                return

    # diagonals
    for i in range(3): # top left to bottom right
        for j in range(4):
            if board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3] == 4:
                misc.winner, misc.gameover, winning_line.game_line_data = 1, True, ('diagonal', i, j, i+3, j+3)
                return
            elif board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3] == -4:
                misc.winner, misc.gameover, winning_line.game_line_data = -1, True, ('diagonal', i, j, i+3, j+3)
                return
    for i in range(3, 6): # bottom left to top right
        for j in range(4):
            if board[i][j] + board[i-1][j+1] + board[i-2][j+2] + board[i-3][j+3] == 4:
                misc.winner, misc.gameover, winning_line.game_line_data = 1, True, ('diagonal', i, j, i-3, j+3)
                return
            elif board[i][j] + board[i-1][j+1] + board[i-2][j+2] + board[i-3][j+3] == -4:
                misc.winner, misc.gameover, winning_line.game_line_data = -1, True, ('diagonal', i, j, i-3, j+3)
                return
    return


def check_for_draws() -> None:
    if misc.turns == 42:
        misc.winner = 0
        misc.gameover = True
