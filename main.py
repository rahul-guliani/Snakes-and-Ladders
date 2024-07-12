from board import roll_a_dice_loop, draw_board_with_player, \
    draw_board_with_ladders

from draw_ladders import draw_ladders




player_position = 0
play_interrupted = False    # if user press a button other than 'r' or 'R's

ladders = draw_ladders(10)
print(ladders)
draw_board_with_ladders(ladders)

draw_board_with_player(player_position)




    









# draw_board()
# play_game()


# ladders_dict = dl.draw_ladders(10)
# ladder_one_ends = ladders_dict['ladder_one_end']
# ladder_other_ends = ladders_dict['ladder_other_end']
# ladders = [(min(ladder_one_ends[i], ladder_other_ends[i]), max(ladder_one_ends[i], ladder_other_ends[i])) for i in range(len(ladder_one_ends))]
# print(ladders)

# def draw_board_with_ladders(ladders_dict):
  
#     for i in range(10):
#         for j in range(10):
#             if (i % 2 == 0):    # If i = 0,2,4,8
#                 box_number = 10*(9-i) + 10-j
#                 if (box_number not in ladders_dict['ladder_one_end']) and (box_number not in ladders_dict['ladder_other_end']):
#                     print(str(box_number).rjust(3), end=' ')  # Add number in decending order (10 to 1) for alternative row starting from first row 
                
#                 elif box_number in ladders_dict['ladder_one_end']:
#                     one_end_index = ladders_dict['ladder_one_end'].index(box_number)
#                     print(f"L{one_end_index + 1}".rjust(3), end=' ')    # adding 1 to the index beacause index starts from zero

#                 else:
#                     other_end_index = ladders_dict['ladder_other_end'].index(box_number)
#                     print(f"L{other_end_index + 1}".rjust(3), end=' ')

#             else:
#                 box_number = 10*(9-i) + 1+j
#                 if (box_number not in ladders_dict['ladder_one_end']) and (box_number not in ladders_dict['ladder_other_end']):
#                     print(str(box_number).rjust(3), end=' ')  # Add number in decending order (10 to 1) for alternative row starting from first row 
                
#                 elif box_number in ladders_dict['ladder_one_end']:
#                     one_end_index = ladders_dict['ladder_one_end'].index(box_number)
#                     print(f"L{one_end_index + 1}".rjust(3), end=' ')

#                 else:
#                     other_end_index = ladders_dict['ladder_other_end'].index(box_number)
#                     print(f"L{other_end_index + 1}".rjust(3), end=' ')
                   
#         print()     # To go to the next line   





