



def game_start(player_position):
    global play_interrupted 
    while(True):
        roll_dice_and_print_board()
        
        if play_interrupted:
            if (input('wanna exit game (y/n) ? :  ').lower()) == 'y':
                break
            
            else:
                play_interrupted = False
       
        if player_position >= 100:
            game_finished()
            break

def game_finished():
    print('Player PPP finished the game.')


def play_game():
    wanna_play_game = input('wanna play game (y/n) ? :  ')
    if wanna_play_game.lower() == 'y':
        game_start()

def roll_dice_and_print_board():
    global play_interrupted
    roll_a_dice = input("Wanna roll the dice (r) ? :  ")
    if roll_a_dice.lower() == 'r':
        final_number = roll_a_dice_loop()
        print(f"Player PPP moves {final_number} {'place' if final_number == 1 else 'places'} forward")
        global player_position 
        player_position += final_number
        # Update Player position if there is a ladder foot on the current player position
            
        # player_position = ladder_heads[ladder_heads.index(player_position)] if player_position in ladder_foots
        draw_board_with_player(player_position)    # Draw board with Player(P) on it at position 'final_number)

    else:
        play_interrupted = True