import misc
from screendisplay import *

class Winning_game_line:

    def __init__(self) -> None:
        self.game_line_data = ("direction", "data")

    def draw_winning_game_line(self):
        if misc.gameover:
            color = (255, 255, 255)
            width = 5
            data = self.game_line_data
            if data[0] == 'horizontal': # data = ('horizontal', rowID, i, i+3)
                start_pos = (board_display.x + data[2] * tile_size + tile_size // 2, board_display.y + data[1] * tile_size + tile_size // 2)
                end_pos = (board_display.x + data[3] * tile_size + tile_size // 2, board_display.y + data[1] * tile_size + tile_size // 2)
                pygame.draw.line(screen, color, start_pos, end_pos, width)
            elif data[0] == 'vertical': # data = ('vertical', i, j, j+3)
                start_pos = (board_display.x + tile_size * data[1] + tile_size // 2, board_display.y + data[2] * tile_size + tile_size // 2)
                end_pos = (board_display.x + tile_size * data[1] + tile_size // 2, board_display.y + data[3] * tile_size + tile_size // 2)
                pygame.draw.line(screen, color, start_pos, end_pos, width)
            elif data[0] == 'diagonal': # data = ('diagonal', i, j, i-3, j+3)
                start_pos = (board_display.x + tile_size * data[2] + tile_size // 2, board_display.y + tile_size * data[1] + tile_size // 2)
                end_pos = (board_display.x + tile_size * data[4] + tile_size // 2, board_display.y + tile_size * data[3] + tile_size // 2)
                pygame.draw.line(screen, color, start_pos, end_pos, width)

winning_line = Winning_game_line()