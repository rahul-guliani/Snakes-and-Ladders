import random

# Draw the Board

'''
11  12  13  14  15  16  17  18  19  20
 1   2   3   4   5   6   7   8   9  10

'''

''' Change the order of number of second row from bottom to "decending" order'''


'''
100  99  98  97  96  95  94  93  92  91
 81  82  83  84  85  86  87  88  89  90
 "
 "
 "
 20  19  18  17  16  15  14  13  12  11
  1   2   3   4   5   6   7   8   9  10
'''

'''
      j=0              j=1             "   "   "   j=8              j=9
    ----------------------------------------------------------------------------------
i=0 | 10(9-0) + 10-0   10(9-0) + 10-1              10(9-0) + 10-8   10(9-0) + 10-9
i=1 | 10(9-1) + 1+0    10(9-1) + 1+1               10(9-1) + 1+8    10(9-1) + 1+9
"   |
"   |
"   |
i=8 | 10(9-8) + 10-0   10(9-8) + 10-1  "   "   "   10(9-8) + 10-8   10(9-8) + 10-9
i=9 | 10(9-9) + 1+0    10(9-9) + 1+1   "   "   "   10(9-9) + 1+8    10(9-9) + 1+9
'''


# Game Board only with numbers
def draw_board():
    for i in range(10):
        for j in range(10):
            if (i % 2 == 0):    # If i = 0,2,4,8 
                box_number = 10*(9-i) + 10-j
                print(str(box_number).center(3), end=' ')  # Add number in decending order (10 to 1) for alternative row starting from first row 
            else:
                box_number = 10*(9-i) + 1+j
                print(str(box_number).center(3), end=' ')     # Add number in ascending order (1 to 10) to 10 times the number of row

        print()     # To go to the next line   


def draw_board_with_player(player_position):
    for i in range(10):
        for j in range(10):
            if (i % 2 == 0):    # If i = 0,2,4,8
                box_number = 10*(9-i) + 10-j
            else:
                box_number = 10*(9-i) + 1+j

            if (player_position != box_number):
                print(str(box_number).center(3), end=' ')  # Add number in decending order (10 to 1) for alternative row starting from first row 
            else:
                print('PPP', end=' ')

        print()     # To go to the next line   


# Roll the dice
'''
number_on_dice = number

number = 6     times_dice_rolled = 1    final_number = 6
number = 6     times_dice_rolled = 2    final_number = 12
number = 6     times_dice_rolled = 3    final_number = 18 
               final_number = 0
               break!

number = 1     times_dice_rolled = 1    final_number = 1
break!

number = 6     times_dice_rolled = 1    final_number = 6
number = 2     times_dice_rolled = 2    final_number = 8
break!

number = 6     times_dice_rolled = 1    final_number = 6
number = 6     times_dice_rolled = 2    final_number = 12
number = 3     times_dice_rolled = 3    final_number = 15
break!

'''

def draw_board_with_ladders(ladders):

    ladder_foots = [ladder[0] for ladder in ladders]    # first element of the each tuple in the list of tuples
    ladder_heads = [ladder[1] for ladder in ladders]    # second element ...
    
    for i in range(10):
        for j in range(10):
            if (i % 2 == 0):    # If i = 0,2,4,8
                box_number = 10*(9-i) + 10-j
            else:
                box_number = 10*(9-i) + 1+j

            if (box_number not in ladder_foots) and (box_number not in ladder_heads):
                print(str(box_number).center(3), end=' ')  # Add number in decending order (10 to 1) for alternative row starting from first row 
            
            elif box_number in ladder_foots:
                ladder_foot_index = ladder_foots.index(box_number)
                print(f'H{ladder_foot_index + 1}'.center(3), end=' ')    # Adding 1 because index starts from zero

            else:
                ladder_head_index = ladder_heads.index(box_number)
                print(f'H{ladder_head_index + 1}'.center(3), end=' ')

        print()     # To go to the next line   


def draw_board_with_ladders_and_players(ladders, snakes, player_1_position, player_2_position):
    ladder_foots = [ladder[0] for ladder in ladders]    # first element of the each tuple in the list of tuples
    ladder_heads = [ladder[1] for ladder in ladders]    # second element ...

    snake_tails = [snake[0] for snake in snakes]
    snake_heads = [snake[1] for snake in snakes]

    for i in range(10):
        row = []
        row_numbers = []
        for j in range(10):
            if (i % 2 == 0):    # If i = 0,2,4,8
                box_number = 10*(9-i) + 10-j
            else:
                box_number = 10*(9-i) + 1+j

            content = ""  # Starts with the empty content for the cell

            # Print ladder_foot with its index
            if box_number in ladder_foots:
                ladder_foot_index = ladder_foots.index(box_number)
                content = f'H{ladder_foot_index + 1}'    # Adding 1 because index starts from zero

            # Print ladder_head with its index
            elif box_number in ladder_heads:
                ladder_head_index = ladder_heads.index(box_number)            
                content = f"H{ladder_head_index + 1}"

            # Print snake_tail
            elif box_number in snake_tails:
                snake_tail_index = snake_tails.index(box_number)
                content = f"S{snake_tail_index + 1}"

            # Print snake_head with its index
            elif box_number in snake_heads:
                snake_head_index = snake_heads.index(box_number)
                content = f"S{snake_head_index + 1}"

            # Print player if it is on the box_number
            if box_number == player_1_position:
                content += 'P1'

            if box_number == player_2_position:
                content = 'P2'


            row.append(content.center(6))
            row_numbers.append(str(box_number).center(6))

        # Print the row content and then the box numbers below it
        print(" ".join(row))
        print(" ".join(row_numbers))
        print("\n")
