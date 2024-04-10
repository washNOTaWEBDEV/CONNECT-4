import pygame
import misc
from screendisplay import *

play_again_rect = pygame.Rect(100, 100, tile_size * 13 // 2, tile_size // 2 + 10)
play_again_rect.center = (screen_width // 2, board_display.y // 2)


for i in range(7):
    exec(f"column_{i}_hover = pygame.Rect(board_display.x + tile_size*{i}, board_display.y, tile_size, board_display.bottom - board_display.y)")
# column_0_hover


def check_for_hover(pos):
    for i in range(7):
        exec(f"""if column_{i}_hover.collidepoint((pos)) and misc.hover == False: misc.hover = True
if column_{i}_hover.collidepoint((pos)) and misc.hover == True: 
    pygame.draw.rect(screen, (150, 150, 180), column_{i}_hover)
    misc.hover = False""")
