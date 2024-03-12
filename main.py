import pygame, sys, pprint
from pygame.locals import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

############################### DISPLAY SETUP #######################################

screen_width = 950
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))

board_width = 560           # 7 tiles
board_height = 480          # 6 tiles
tile_size = board_width//7  # 80 pixels

board_display = pygame.Rect(0,0, board_width, board_height)
board_display.center = (screen_width//2, screen_height//2 - 10)

def draw_grid_lines():
    color = (0, 200, 0)
    width = 2
    for i in range(7):
        pygame.draw.line(screen, color, (board_display.x, board_display.y + tile_size*i), (board_display.right, board_display.y + tile_size*i), width)
    for i in range(8):
        pygame.draw.line(screen, color, (board_display.x + tile_size*i, board_display.y), (board_display.x + tile_size*i, board_display.bottom), width)

########################### MISCELLANEOUS GAME GLOBALS #############################

clicked = False
player = 1
turns = 0 
gameover = False
winner = 0

################################## BOARD SETUP #####################################

class Game:
    def __init__(self, gamenumber):
        self.board = []
        self.board_last_filled_up_indexes = [5] * 7
        self.gamenumber = gamenumber


    def reset_board(self):
        self.board = []

        for _ in range(6):
            self.board.append([0]*7)
        
    
    def draw_board(self):
        red_player_coin = pygame.image.load('red icon.png')
        yellow_player_coin = pygame.image.load('yellow icon.png')

        red_coin_img = pygame.transform.scale(red_player_coin, (tile_size, tile_size))
        yellow_coin_img = pygame.transform.scale(yellow_player_coin, (tile_size, tile_size))

        for rowID, row in enumerate(self.board):
            for columnID, item in enumerate(row):
                if item == 1:
                    screen.blit(red_coin_img, (board_display.x + columnID*tile_size, board_display.y + rowID*tile_size))
                elif item == -1:
                    screen.blit(yellow_coin_img, (board_display.x + columnID*tile_size, board_display.y + rowID*tile_size))

def end_turn(player_number, columnID):
    global turns, player
    connect4.board[connect4.board_last_filled_up_indexes[columnID]][columnID] = player_number
    connect4.board_last_filled_up_indexes[columnID] -=1
    player *= -1
    turns += 1
    return

def check_gameover():
    global gameover, winner

    board = connect4.board

    # rows
    for row in board:
        for i in range(4):
            if row[i] + row[i+1] + row[i+2] + row[i+3] == 4:
                winner, gameover = 1, True
                return
            elif row[i] + row[i+1] + row[i+2] + row[i+3] == -4:
                winner, gameover = -1, True
                return
    # columns
    for i in range(7):
        for j in range(3):
            if board[j][i] + board[j+1][i] + board[j+2][i] + board[j+3][i] == 4:
                winner, gameover = 1, True
                return
            elif board[j][i] + board[j+1][i] + board[j+2][i] + board[j+3][i] == -4:
                winner, gameover = -1, True
                return
    # diagonals
    for i in range(3): # top left to bottom right
        for j in range(4):
            if board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3] == 4:
                winner, gameover = 1, True
                return
            elif board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3] == -4:
                winner, gameover = -1, True
                return
    for i in range(3, 6): # bottom left to top right
        for j in range(4):
            if board[i][j] + board[i-1][j+1] + board[i-2][j+2] + board[i-3][j+3] == 4:
                winner, gameover = 1, True
                return
            elif board[i][j] + board[i-1][j+1] + board[i-2][j+2] + board[i-3][j+3] == -4:
                winner, gameover = -1, True
                return
    return

def check_for_draws():
    global winner, gameover, turns
    if turns == 42:
        winner = 0
        gameover = True
    return

connect4 = Game(0)

connect4.reset_board()

# connect4.board = [
#  [0, 0, 0, 0, 0, , -1],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, -1, -1, 1]]

################################# GAME LOOP ########################################

run = True
while run:

    screen.fill((20,5,20))
    screen.fill((200, 170, 200), board_display)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if gameover == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            elif event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False

                pos = pygame.mouse.get_pos() # (x, y) for mouse position
                pos = ((pos[0] - board_display.x)//tile_size, pos[1]-board_display.bottom) # adjusted to connect 4 board x tiles
                if -1 < pos[0] < 7 and pos[1] < 15 and connect4.board_last_filled_up_indexes[pos[0]] > -1: # 7 is tiles, 15 is pixels

                    if player == 1:
                        end_turn(1, pos[0])
                        check_gameover()
                        if not gameover:
                            check_for_draws()

                    elif player == -1:
                        end_turn(-1, pos[0])
                        check_gameover()
                        if not gameover:
                            check_for_draws()

    if gameover:
        print(f'THE WINNER IS {winner}')


    connect4.draw_board()
    draw_grid_lines()



    pygame.display.flip()
    clock.tick(15)

pygame.quit()