"""
1) Let'say ladder at random positions
2) Ladder can not start from last row (91 to 100)
3) Each ladder must end a row above or rows above that not at the same row where it started
4) If there is already a ladder, starting or ending in a number_box, there can not be another ladder starting or ending.
5)
"""

import random



def draw_ladders_and_snakes(number_of_ladders, numbers_of_snakes):
    ladder_foots = []
    ladder_heads = []

    snake_tails = []
    snake_heads = []

    # To calculate the minimum value the Ladder's head or Snake's foot can have
    # That is the from any value from the next row where the ladder's foot is or snake's tail is 
    def calculate_threshold(value):
        base_value = int(value / 10) * 10
        return base_value + 10 if value % 10 != 0 else value
    
    for i in range(number_of_ladders):
        choices = [
            num 
            for num in range(1, 91)     # Foot cannot be at the top row
            if num not in ladder_foots and
                num not in ladder_heads]
        
        ladder_foot = random.choice(choices)
        ladder_foots.append(ladder_foot)
        # ladder_other_end.append(random.choice([num for num in list(range(1, 101)) if num not in ladder_one_end and num not in ladder_other_end]))

        # Ladder_one_end and other_end must be on different row of the board
        choices = [
            num 
            for num in range(11, 101)       # Head cannot be at the first row
            if num not in ladder_foots and
                num not in ladder_heads and 
                num > calculate_threshold(ladder_foot)]
                # num > (int(ladder_one_end[i]/10) * 10 + 10 if ladder_one_end[i] % 10 != 0 else ladder_one_end[i])]
        
        ladder_head = random.choice(choices)
        ladder_heads.append(ladder_head)
    
    
    ladders = [(ladder_foots[i], ladder_heads[i]) for i in range(len(ladder_foots))]

    # For total no. of snakes
    for i in range(numbers_of_snakes):

        # For snake's tail
        choices = [
            num
            for num in range(1, 91)
            if num not in snake_tails and 
            num not in snake_heads and
            num not in ladder_foots and
            num not in ladder_heads
        ]
        snake_tail = random.choice(choices)
        snake_tails.append(snake_tail)

        # For snake's head
        choices = [
            num 
            for num in range(11, 100)
            if num not in snake_tails and 
            num not in snake_heads and
            num not in ladder_foots and
            num not in ladder_heads and
            num > calculate_threshold(snake_tail)
        ]
        snake_head = random.choice(choices)
        snake_heads.append(snake_head)
    
    snakes = [(snake_tails[i], snake_heads[i]) for i in range(len(snake_tails))]

    return {'snakes': snakes, 'ladders': ladders}


# Ladder_one_end and other_end must have a minimum difference of 2
# Ladder_one_end and other_end must be on different row of the board

# ladder_other_end.append(random.choice([num for num in list(range(1, 101)) if num not in ladder_one_end and num not in ladder_other_end and num not in list(range(int(ladder_one_end[i]/10) * 10) + 1,  (int(ladder_one_end[i]/10) * 10) + 11)]

# def remove_occured_numbers(numers_occured):
    

# for i in range(number_of_ladders):
#     ladder_one_end = (random.choice())

