import pygame, sys, pprint
from pygame.locals import *

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

############################### DISPLAY SETUP #######################################

font = pygame.font.SysFont('dnpshueiminchopr6b', 35)

screen_width = 950
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))

board_width = 560           # 7 tiles
board_height = 480          # 6 tiles
tile_size = board_width//7  # 80 pixels

board_display = pygame.Rect(0,0, board_width, board_height)
board_display.center = (screen_width//2, screen_height//2 - 10)

class Frametype:
    def __init__(self, filename, tile_data) -> None:
        self.name = filename
        self.img = pygame.image.load(f'{filename}')
        self.img = pygame.transform.scale(self.img, (tile_size, tile_size))
        self.tile_data = tile_data 
    def draw_frame_for_oneself(self):
        screen.blit(self.img,  (board_display.x + tile_size* self.tile_data[1], board_display.y + tile_size*self.tile_data[0]))
 
normalframe = Frametype('connect4frame.png', (1,1))

def draw_grid_lines():
    for i in range(6):
        for j in range(7):
            screen.blit(normalframe.img,  (board_display.x + tile_size*j, board_display.y + tile_size*i))

        
########################### MISCELLANEOUS GAME GLOBALS #############################

clicked = False
hover = False
player = 1
turns = 0 
gameover = False
winner = 0
play_again_rect = pygame.Rect(100, 100, tile_size*13 // 2, tile_size//2 + 10)
play_again_rect.center = (screen_width//2, board_display.y//2)
################################## BOARD SETUP #####################################

class Game:
    def __init__(self, gamenumber):
        self.board = []
        self.board_last_filled_up_indexes = [5] * 7
        self.gamenumber = gamenumber


    def reset_board(self):
        self.board = []
        self.board_last_filled_up_indexes = [5] * 7

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

for i in range(7):
    exec(f'column_{i}_hover = pygame.Rect(board_display.x + tile_size*{i}, board_display.y, tile_size, board_display.bottom - board_display.y)')
# column_0_hover

def check_for_hover():
    global hover
    for i in range(7):
        exec(f'''if column_{i}_hover.collidepoint((pos)) and hover == False: hover = True
if column_{i}_hover.collidepoint((pos)) and hover == True: 
    pygame.draw.rect(screen, (150, 150, 180), column_{i}_hover)
    hover = False''')

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
    for rowID, row in enumerate(board):
        for i in range(4):
            if row[i] + row[i+1] + row[i+2] + row[i+3] == 4:
                winner, gameover, winning_line.game_line_data = 1, True, ('horizontal', rowID, i, i+3) 
                return
            elif row[i] + row[i+1] + row[i+2] + row[i+3] == -4:
                winner, gameover, winning_line.game_line_data = -1, True, ('horizontal', rowID, i, i+3) 
                return
    # columns
    for i in range(7):
        for j in range(3):
            if board[j][i] + board[j+1][i] + board[j+2][i] + board[j+3][i] == 4:
                winner, gameover, winning_line.game_line_data = 1, True, ('vertical', i, j, j+3)
                return
            elif board[j][i] + board[j+1][i] + board[j+2][i] + board[j+3][i] == -4:
                winner, gameover, winning_line.game_line_data = -1, True, ('vertical', i, j, j+3)
                return
    # diagonals
    for i in range(3): # top left to bottom right
        for j in range(4):
            if board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3] == 4:
                winner, gameover, winning_line.game_line_data = 1, True, ('diagonal', i, j, i+3, j+3)
                return
            elif board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3] == -4:
                winner, gameover, winning_line.game_line_data = -1, True, ('diagonal', i, j, i+3, j+3)
                return
    for i in range(3, 6): # bottom left to top right
        for j in range(4):
            if board[i][j] + board[i-1][j+1] + board[i-2][j+2] + board[i-3][j+3] == 4:
                winner, gameover, winning_line.game_line_data = 1, True, ('diagonal', i, j, i-3, j+3)
                return
            elif board[i][j] + board[i-1][j+1] + board[i-2][j+2] + board[i-3][j+3] == -4:
                winner, gameover, winning_line.game_line_data = -1, True, ('diagonal', i, j, i-3, j+3)
                return
    return

def check_for_draws() -> None:
    global winner, gameover, turns
    if turns == 42:
        winner = 0
        gameover = True

class Winning_game_line:
    global gameover
    def __init__(self) -> None:
        self.game_line_data = ('direction', 'data')

    def draw_winning_game_line(self):
        if gameover:
            color = (255, 255, 255)
            width = 5
            data = self.game_line_data
            if data[0] == 'horizontal': # data = ('horizontal', rowID, i, i+3)
                start_pos = (board_display.x + data[2] * tile_size + tile_size//2, board_display.y + data[1]*tile_size + tile_size//2)
                end_pos = (board_display.x + data[3] * tile_size + tile_size//2, board_display.y + data[1]*tile_size + tile_size//2)
                pygame.draw.line(screen, color, start_pos, end_pos, width)
            elif data[0] == 'vertical': # data = ('vertical', i, j, j+3)
                start_pos = (board_display.x + tile_size * data[1] + tile_size//2, board_display.y + data[2] * tile_size + tile_size//2)
                end_pos = (board_display.x + tile_size * data[1] + tile_size//2, board_display.y + data[3] * tile_size + tile_size//2)
                pygame.draw.line(screen, color, start_pos, end_pos, width)
            elif data[0] == 'diagonal': # data = ('diagonal', i, j, i-3, j+3)
                start_pos = (board_display.x + tile_size * data[2] + tile_size//2, board_display.y + tile_size * data[1] + tile_size//2)
                end_pos = (board_display.x + tile_size * data[4] + tile_size//2, board_display.y + tile_size * data[3] + tile_size//2)
                pygame.draw.line(screen, color, start_pos, end_pos, width)

winning_line = Winning_game_line()
    

def end_of_game():
    if winner == 1:
        end_text = '試合終了。The reds have won!'
    elif winner == -1:
        end_text = '試合終了。The yellows have won!'
    else:
        end_text = 'なんてこった！drawなのだ！'

    ending_text_bottom = font.render(end_text, False, (30, 20, 30))
    center_ending_text_bottom = ending_text_bottom.get_rect()
    center_ending_text_bottom.center = (screen_width//2, board_display.bottom + (screen_height - board_display.bottom)//2)
    screen.blit(ending_text_bottom, center_ending_text_bottom)

def ask_to_play_again():
    if winner == 1:
        play_again_text = 'red ready the red red reed rawr'
    elif winner == -1:
        play_again_text = 'ye yet yoo yada yuck it\'s you'
    else:
        play_again_text = 'つまんないよね、このゲーム'

    play_again_text = font.render(play_again_text, False, (225, 225, 225))
    center_play_again_text = play_again_text.get_rect()
    center_play_again_text.center = (screen_width//2, board_display.y//2)
    pygame.draw.rect(screen, (50, 50, 80), play_again_rect)
    screen.blit(play_again_text, center_play_again_text)
    


connect4 = Game(0)

connect4.reset_board()

################################# GAME LOOP ########################################

run = True

board_color = (230, 220, 234)
screen.fill((230,220,234))
screen.fill(board_color, board_display)

while run:


    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if hover == False:
            screen.fill((230,220,234))
            screen.fill(board_color, board_display)
            check_for_hover()

        if gameover == False:

            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            elif event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False

                # pos = (x, y) for mouse position
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


    connect4.draw_board()
    draw_grid_lines()


    if gameover:
        end_of_game()
        winning_line.draw_winning_game_line()
        ask_to_play_again()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            if play_again_rect.collidepoint(pygame.mouse.get_pos()):
                gameover = False
                player = 1
                turns = 0 
                winner = 0
                clicked = False
                hover = False
                winning_line.game_line_data = ('direction', 'default settings')
                pygame.mouse.set_pos(tuple(map(lambda x: x+1, pygame.mouse.get_pos())))
                connect4.reset_board()


    pygame.display.flip()
    clock.tick(20)

pygame.quit()