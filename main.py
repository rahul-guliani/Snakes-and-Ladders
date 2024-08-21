from game_stages import play_game
from board import draw_board_with_ladders

from draw_ladders import draw_ladders




player_position = 0
play_interrupted = False    # if user press a button other than 'r' or 'R's

ladders = draw_ladders(10)
print(ladders)
draw_board_with_ladders(ladders)


play_game()

