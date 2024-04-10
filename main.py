import pygame
import sys
import misc
from screendisplay import *
from draw_frames import draw_grid_lines
from game_board import connect4
import hover_columns 
from end_game import end_turn, check_gameover, check_for_draws
from winning_game_line import winning_line
from resetgame import end_of_game, ask_to_play_again

pygame.init()
clock = pygame.time.Clock()

################################# GAME LOOP ########################################

run = True

board_color = (230, 220, 234)
screen.fill((230, 220, 234))
screen.fill(board_color, board_display)

while run:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if misc.hover is False:
            screen.fill((230, 220, 234))
            screen.fill(board_color, board_display)
            hover_columns.check_for_hover(pos)

        if misc.gameover is False:
            if event.type == pygame.MOUSEBUTTONDOWN and misc.clicked is False:
                misc.clicked = True
            elif event.type == pygame.MOUSEBUTTONUP and misc.clicked:
                misc.clicked = False

                # pos = (x, y) for mouse position
                pos = ((pos[0] - board_display.x) // tile_size, pos[1] - board_display.bottom) # adjusted to connect 4 board x tiles
                if -1 < pos[0] < 7 and pos[1] < 15 and connect4.board_last_filled_up_indexes[pos[0]] > -1:  # 7 is tiles, 15 is pixels
                    # print(f"player is {player}")
                    if misc.player == 1:
                        end_turn(1, pos[0])
                        check_gameover()
                        if not misc.gameover:
                            check_for_draws()

                    elif misc.player == -1:
                        end_turn(-1, pos[0])
                        check_gameover()
                        if not misc.gameover:
                            check_for_draws()

    connect4.draw_board()
    draw_grid_lines()

    if misc.gameover:
        end_of_game()
        winning_line.draw_winning_game_line()
        ask_to_play_again()
        if event.type == pygame.MOUSEBUTTONDOWN and misc.clicked is False:
            misc.clicked = True
        if event.type == pygame.MOUSEBUTTONUP and misc.clicked:
            misc.clicked = False
            if hover_columns.play_again_rect.collidepoint(pygame.mouse.get_pos()):
                misc.gameover = False
                misc.player = 1
                misc.turns = 0
                misc.winner = 0
                misc.clicked = False
                misc.hover = False
                winning_line.game_line_data = ("direction", "default settings")
                connect4.reset_board()
                connect4.draw_board()
                # screen.fill((230, 220, 234)) WORKS BUT THERE'S A FLASH AND IT HURTS MY EYES, SO IMMA JUST MOVE THE MOUSE 
                pygame.mouse.set_pos((pos[0]+1, pos[1]+1))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()