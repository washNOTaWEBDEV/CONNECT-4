import misc
from screendisplay import *
from hover_columns import play_again_rect

def end_of_game():
    if misc.winner == 1:
        end_text = "試合終了。The reds have won!"
    elif misc.winner == -1:
        end_text = "試合終了。The yellows have won!"
    else:
        end_text = "なんてこった！drawなのだ！"

    ending_text_bottom = font.render(end_text, False, (30, 20, 30))
    center_ending_text_bottom = ending_text_bottom.get_rect()
    center_ending_text_bottom.center = (screen_width // 2, board_display.bottom + (screen_height - board_display.bottom) // 2)
    screen.blit(ending_text_bottom, center_ending_text_bottom)

def ask_to_play_again():
    play_again_text = "Click to play again!"
    # if misc.winner == 1:
    #     play_again_text = "red ready the red red reed rawr"
    # elif misc.winner == -1:
    #     play_again_text = "ye yet yoo yada yuck it's you"
    # else:
    #     play_again_text = "つまんないよね、このゲーム"

    play_again_text = font.render(play_again_text, False, (225, 225, 225))
    center_play_again_text = play_again_text.get_rect()
    center_play_again_text.center = (screen_width // 2, board_display.y // 2)
    pygame.draw.rect(screen, (50, 50, 80), play_again_rect)
    screen.blit(play_again_text, center_play_again_text)
