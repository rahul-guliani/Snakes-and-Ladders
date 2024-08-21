from board import draw_board_with_player
import random



def game_start():
    
    player_position = 0
    while(True):
        # Call the roll_dice_and_print_board() and receives the returned dictionary in a variable 
        returned_dict = roll_dice_and_print_board(player_position)     # function executes 
        play_interruption = returned_dict['play_interruption']
        final_number = returned_dict['final_number']
        
        # Update the player_position
        player_position += final_number

        if play_interruption:
            if (input('wanna exit game (y/n) ? :  ').lower()) == 'y':
                break
            
            else:
                play_interruption = False
       
        if player_position >= 100:
            game_finished()
            break

def game_finished():
    print('Player PPP finished the game.')


def play_game():
    wanna_play_game = input('wanna play game (y/n) ? :  ')
    if wanna_play_game.lower() == 'y':
        game_start()

def roll_dice_and_print_board(player_position):
    play_interruption = False
    roll_a_dice = input("Wanna roll the dice (r) ? :  ")
    if roll_a_dice.lower() == 'r':
        final_number = roll_a_dice_loop()
        print(f"Player PPP moves {final_number} {'place' if final_number == 1 else 'places'} forward")
        # global player_position 
        player_position += final_number
        # Update Player position if there is a ladder foot on the current player position
            
        # player_position = ladder_heads[ladder_heads.index(player_position)] if player_position in ladder_foots
        draw_board_with_player(player_position)    # Draw board with Player(P) on it at position 'final_number)

    else:
        play_interruption = True     # If game interrupted by preesing any key other than 'r' or 'R'
        final_number = 0             # If game is interrupted, final number rolled is 0 

    return {'play_interruption': play_interruption, 'final_number': final_number}  



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