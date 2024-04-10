from misc import *
from screendisplay import *

class Frametype:
    def __init__(self, filename, tile_data) -> None:
        self.name = filename
        self.img = pygame.image.load(f"{filename}")
        self.img = pygame.transform.scale(self.img, (tile_size, tile_size))
        self.tile_data = tile_data

    def draw_frame_for_yourself(self):
        screen.blit(self.img,  (board_display.x + tile_size * self.tile_data[1], board_display.y + tile_size * self.tile_data[0]))
 
normalframe = Frametype('./images/connect4frame.png', (1,1))
bottomleftframe = Frametype('./images/bottomleftframe.png', (5, -1))
bottomrightframe = Frametype('./images/bottomrightframe.png', (5, 7))
leftsideframe = Frametype('./images/leftsideframe.png', (6, -1))
rightsideframe = Frametype('./images/rightsideframe.png', (6, -1))

def draw_grid_lines():
    for i in range(6):
        if i != 5:
            screen.blit(leftsideframe.img, (board_display.x - tile_size, board_display.y + tile_size * i))
            screen.blit(rightsideframe.img, (board_display.right, board_display.y + tile_size * i))
        for j in range(7):
            screen.blit(normalframe.img, (board_display.x + tile_size * j, board_display.y + tile_size * i))
    bottomrightframe.draw_frame_for_yourself()
    bottomleftframe.draw_frame_for_yourself()