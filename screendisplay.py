import pygame

pygame.font.init()
font = pygame.font.SysFont("dnpshueiminchopr6b", 35)

screen_width, screen_height = 950, 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Connect 4')

board_width = 560  # 7 tiles
board_height = 480  # 6 tiles
tile_size = board_width // 7  # 80 pixels

board_display = pygame.Rect(0, 0, board_width, board_height)
board_display.center = (screen_width // 2, screen_height // 2 - 10)