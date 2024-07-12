player_position = 32

ladder_foots = [23, 43, 76, 32, 82, 64, 18]
ladder_heads = [54, 67, 91, 78, 99, 84, 36]

if player_position in ladder_foots:
    index = ladder_foots.index(player_position)
    player_position = ladder_heads[index]