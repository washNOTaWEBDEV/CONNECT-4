import pygame
import misc
from screendisplay import screen, screen_width, tile_size, board_display

pygame.init()

class Game:
    def __init__(self, gamenumber):
        self.board = []
        self.board_last_filled_up_indexes = [5] * 7
        self.gamenumber = gamenumber

    def reset_board(self):
        self.board = []
        self.board_last_filled_up_indexes = [5] * 7

        for _ in range(6):
            self.board.append([0] * 7)

    def draw_board(self):
        red_player_coin = pygame.image.load('./images/red icon.png')
        yellow_player_coin = pygame.image.load('./images/yellow icon.png')

        red_coin_img = pygame.transform.scale(red_player_coin, (tile_size, tile_size))
        yellow_coin_img = pygame.transform.scale(yellow_player_coin, (tile_size, tile_size))

        if misc.player == 1 and not misc.gameover:
            screen.blit(red_coin_img, (0, 0))
            screen.blit(red_coin_img, (screen_width-tile_size, 0))
        elif misc.player == -1 and not misc.gameover:
            screen.blit(yellow_coin_img, (0, 0))
            screen.blit(yellow_coin_img, (screen_width-tile_size, 0))

        # print(self.board)
        for rowID, row in enumerate(self.board):
            for columnID, item in enumerate(row):
                if item == 1:
                    screen.blit(red_coin_img, (board_display.x + columnID * tile_size, board_display.y + rowID * tile_size))
                elif item == -1:
                    screen.blit(yellow_coin_img, (board_display.x + columnID * tile_size, board_display.y + rowID * tile_size))

connect4 = Game(0)

connect4.reset_board()