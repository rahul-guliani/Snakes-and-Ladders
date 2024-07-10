"""
1) Let'say ladder at random positions
2) Ladder can not start from last row (91 to 100)
3) Each ladder must end a row above or rows above that not at the same row where it started
4) If there is already a ladder, starting or ending in a number_box, there can not be another ladder starting or ending.
5)
"""

import random

random_number_occured = []

number_of_ladders = 10
ladder_one_end = []
ladder_other_end = []

for i in range(number_of_ladders):
    ladder_one_end.append(random.choice([num for num in range(1, 101) if num not in ladder_one_end and num not in ladder_other_end]))
    # ladder_other_end.append(random.choice([num for num in list(range(1, 101)) if num not in ladder_one_end and num not in ladder_other_end]))

    # Ladder_one_end and other_end must be on different row of the board
    ladder_other_end.append(random.choice([num for num in range(1, 101) if num not in ladder_one_end and num not in ladder_other_end and num not in range((int(ladder_one_end[i]/10) * 10) + 1,  (int(ladder_one_end[i]/10) * 10) + 11)]))

print(ladder_one_end)
print(ladder_other_end)


# Ladder_one_end and other_end must have a minimum difference of 2
# Ladder_one_end and other_end must be on different row of the board

# ladder_other_end.append(random.choice([num for num in list(range(1, 101)) if num not in ladder_one_end and num not in ladder_other_end and num not in list(range(int(ladder_one_end[i]/10) * 10) + 1,  (int(ladder_one_end[i]/10) * 10) + 11)]

# def remove_occured_numbers(numers_occured):
    

# for i in range(number_of_ladders):
#     ladder_one_end = (random.choice())

