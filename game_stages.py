from board import draw_board_with_ladders_and_players
from draw_ladders import draw_ladders_and_snakes
import random



def game_start():

    snakes_and_ladders_dict = draw_ladders_and_snakes(10, 10)
    snakes = snakes_and_ladders_dict['snakes']
    ladders = snakes_and_ladders_dict['ladders']
    
    player_1_position = 0
    player_2_position = 0

    while(True):
        # Call the roll_dice() and receives the returned dictionary in a variable 

        print(f"----------PLAYER_1-----------")
        returned_dict_player_1 = roll_dice()     # function executes 
        player_1_interruption = returned_dict_player_1['play_interruption']
        if player_1_interruption:
            if (input('wanna exit game (y/n) ? :  ').lower()) == 'y':
                break
        player_1_rolled_number = returned_dict_player_1['total_number_rolled']
        player_1_position += player_1_rolled_number

        # Draw Board
        draw_board_with_ladders_and_players(snakes=snakes, ladders=ladders, player_1_position=player_1_position, player_2_position=player_2_position)

        print(f"----------PLAYER_2-----------")
        returned_dict_player_2 = roll_dice()
        player_2_interruption = returned_dict_player_2['play_interruption']
        if player_2_interruption:
            if (input('wanna exit game (y/n) ? :  ').lower()) == 'y':
                break
        player_2_rolled_number = returned_dict_player_2['total_number_rolled']
        player_2_position += player_2_rolled_number
        
        # Draw Board
        draw_board_with_ladders_and_players(snakes=snakes, ladders=ladders, player_1_position=player_1_position, player_2_position=player_2_position)


        # Update the player_position
        # player_position += final_number
    
        if player_1_position >= 100:
            game_finished('player_1')
            break

        elif player_2_position >= 100:
            game_finished('player_2')
            break

def game_finished(player):
    print(f'Player {player} finished the game.')


def play_game():
    wanna_play_game = input('wanna play game (y/n) ? :  ')
    if wanna_play_game.lower() == 'y':
        game_start()

def roll_dice():

    # ladder_foots = [ladder[0] for ladder in ladders]    # first element of the each tuple in the list of tuples
    # ladder_heads = [ladder[1] for ladder in ladders]    # second element ...

    # snake_tails = [snake[0] for snake in snakes]
    # snake_heads = [snake[1] for snake in snakes]

    play_interruption = False
    roll_a_dice = input("Wanna roll the dice (r) ? :  ")
    if roll_a_dice.lower() == 'r':
        final_number = roll_a_dice_loop()
        # player_position += final_number
        # print(f"{player} moves {final_number} {'place' if final_number == 1 else 'places'} forward to box-number: {player_position}")

    
        # Update Player position if there is a ladder foot on the current player position 
        # if player_position in ladder_foots:
        #     player_position = ladder_heads[ladder_foots.index(player_position)]   # head at same index where foot is
        #     print(f"your player is on a ladder's foot, happy to move it to its head that is box-number: {player_position}")

        # if player_position in snake_heads:
        #     player_position = snake_tails[snake_heads.index(player_position)]   # tail at same index where head is
        #     print(f"Your player is on a snake's head, so sorry to take you to its tail that is box-number: {player_position}")

        # draw_board_with_ladders_and_players(ladders, snakes, player_position)    # Draw board with Player(P) on it at position 'player_position')


    else:
        play_interruption = True     # If game interrupted by preesing any key other than 'r' or 'R'
        final_number = 0             # If game is interrupted, final number rolled is 0 

    return {'play_interruption': play_interruption, 'total_number_rolled': final_number}  



def roll_a_dice_loop():
    times_dice_rolled = 0
    final_number = 0
    while(True):
        number_on_dice = random.randint(1,6)
        times_dice_rolled += 1

        # Print the number came by rolling dice
        if times_dice_rolled == 1:
            print("Number Rolled :  ", number_on_dice)
        elif times_dice_rolled == 2:
            print("Second Number Rolled :  ", number_on_dice)
        else:
            print("Third Number Rolled :  ", number_on_dice)
        
        # Final_number will be total of previous number rolled plus the number rolled this time
        final_number += number_on_dice

        # If number on dice rolled is 6, loop wil continue to roll the dice next time otherwise break
        if (number_on_dice != 6) :
            break

        # if dice rolled 3 times and loop already not broke, that means third number also is 6
        if (times_dice_rolled >= 3):
            final_number = 0
            print("Your Turn vanished!")
            break
    return final_number
