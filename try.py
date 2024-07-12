<<<<<<< HEAD
player_position = 32

ladder_foots = [23, 43, 76, 32, 82, 64, 18]
ladder_heads = [54, 67, 91, 78, 99, 84, 36]

if player_position in ladder_foots:
    index = ladder_foots.index(player_position)
    player_position = ladder_heads[index]
=======
my_list = [2, 5, 2, 6]

my_list = [i for i in range(10)]

print(my_list)


ladder_foots = [34, 29, 54, 23, 32, 12, 21]
ladder_heads = [53, 81, 67, 63, 73, 71, 85]

player_position = 32

if player_position in ladder_foots:
    index = ladder_foots.index(player_position, 1)
    player_position = ladder_heads[index]

print(player_position)
>>>>>>> d63fb6037fc888b9fc3f5025d6c9adb6598e3272
