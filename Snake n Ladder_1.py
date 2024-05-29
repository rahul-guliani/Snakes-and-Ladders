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
                print(str(10*(9-i) + 10-j).rjust(3), end=' ')  # Add number in decending order (10 to 1) for alternative row starting from first row 
            else:
                print(str(10*(9-i) + 1+j).rjust(3), end=' ')     # Add number in ascending order (1 to 10) to 10 times the number of row

        print()     # To go to the next line   


def draw_board_with_player(player_position_number):
    for i in range(10):
        for j in range(10):
            if (i % 2 == 0):    # If i = 0,2,4,8
                if (player_position_number != 10*(9-i) + 10-j):
                    print(str(10*(9-i) + 10-j).rjust(3), end=' ')  # Add number in decending order (10 to 1) for alternative row starting from first row 
                else:
                    print('PPP', end=' ')
            else:
                if (player_position_number != 10*(9-i) + 1+j):
                    print(str(10*(9-i) + 1+j).rjust(3), end=' ')     # Add number in ascending order (1 to 10) to 10 times the number of row
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


final_number = 0
times_dice_rolled = 0

# Following while loop will add the consecutive third time six to the final_number before assigning zero
while(True):
    number_on_dice = random.randint(1,6)
    times_dice_rolled += 1
    final_number += number_on_dice

    if (number_on_dice != 6) :
        break
    elif (times_dice_rolled >= 3):
        final_number = 0
        break

# Following while loop will NOT add the consecutive third time six to the final number instead it wil assign zero to the final_number directly
"""
while(True):
    number_on_dice = random.randint(1,6)
    times_dice_rolled += 1
    if ((times_dice_rolled == 3) and (number_on_dice == 6)):
        final_number = 0
        break
    
    final_number += number_on_dice

    if (number_on_dice != 6) :
        break
"""
 
    
draw_board()
print(final_number)
draw_board_with_player(final_number)

# Draw board with Player(P) on it at position 'final_number)


'''
num = 0
while(True):
    print(num)
    num += 1
    if (num == 2):   
        break

print('outside_num = ', num)
'''

