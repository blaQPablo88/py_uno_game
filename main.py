import random

# deck of cards
cards = []
last_played_cards = []
players_hand = []
comps_hand = []
n_start_cards = 7
turn_to_play = 1
# card colors
colors = ['red', 'green', 'blue', 'yellow']

# wildcards list
action = ['reverse', 'skip', 'draw 2']

# creating the deck
for color in colors:
    for card_num in range(10):
        card = f'{color}_{card_num}'
        if card_num == 0:
            cards.append(card)
        else:
            cards.append(card)  # this for cards 1 to 9
            cards.append(card)

    # getting the action cards
    for x in action:
        card = f'{color}_{x}'
        cards.append(card)
        cards.append(card)

# creating wild cards
for _ in range(4):
    cards.append('wild_card')
    cards.append('wild_draw 4')

# initialize hands (player & comp)
players_hand = random.sample(cards, n_start_cards)
for x in players_hand:
    cards.remove(x)

comps_hand = random.sample(cards, n_start_cards)
for x in comps_hand:
    cards.remove(x)

# shuffling function
def shuffle_deck(deck):
    # turn_to_play += 1
    random.shuffle(deck)
    
shuffle_deck(cards)
# skip next player
def skipping_card(turn_to_play):
    return turn_to_play
    
# color changing function
def wild_color_card():
    if turn_to_play % 2 == 0:
        comp_selected_color = random.choice(colors)  # Computer randomly chooses a color
        print(f"Comp played a Wild card! And chose: {comp_selected_color}")
        last_played_cards.append(f'{comp_selected_color}_wild')
    else:
        print("You played a Wild card! Choose a color:")
        for idx, color in enumerate(colors, 1):
            print(f'{idx}. {color}')
        user_input = input('Choose a color (1-4): ')
        while True:
            if user_input.isdigit() and 1 <= int(user_input) <= 4:
                selected_color = colors[int(user_input) - 1]
                print(f'You chose {selected_color} as the next color.')
                last_played_cards.append(f'{selected_color}_wild')
                break
            else:
                user_input = input("Invalid choice, choose a number between 1 and 4: ")

# draw_2 function
def draw_2():
    drawn_cards = cards[:2]
    del cards[:2]
    if turn_to_play % 2 == 0:
        comps_hand.extend(drawn_cards)
        print(f"Comp draws: {drawn_cards}")
    else:
        players_hand.extend(drawn_cards)
        print(f"Player draws: {drawn_cards}")

# draw_4 function
def draw_4():
    drawn_cards = cards[:4]
    del cards[:4]
    if turn_to_play % 2 == 0:
        comps_hand.extend(drawn_cards)
        print(f"Comp draws: {drawn_cards}")
    else:
        players_hand.extend(drawn_cards)
        print(f"Player draws: {drawn_cards}")

# check and validate top card
def get_top_card_details(selected_card):
    last_played_card = last_played_cards[-1]
    card_suffix = last_played_card.split('_')[1]
    if card_suffix == 'card':
        print(f'{last_played_card} - Wild Card')
        wild_color_card()
        last_played_cards.remove(last_played_card)
    elif selected_card.split('_')[0] == last_played_card.split('_')[0] or selected_card.split('_')[1] == last_played_card.split('_')[1] or selected_card.split('_')[1] == 'draw 4' or selected_card.split('_')[1] == 'card':
        # print('Valid play!')
        return True  # Return True for a valid play
    else:
        # print('Invalid play! Draw a card.')
        return False
    print(f'Top card: {last_played_card}')

# player/user turn
def players_turn():
    global turn_to_play
    print("\nYour turn!")
    # print(f"Your hand: {players_hand}")

    for i, player_card_hand in enumerate(players_hand):
        print(f'{i + 1}. {player_card_hand}')

    user_input = input(f'Choose a card (1-{len(players_hand)}): ')
    
    while True:
        if user_input.isdigit() and 1 <= int(user_input) <= len(players_hand):
            selected_card = players_hand[int(user_input) - 1]
            print(f'You played {selected_card}')
            if get_top_card_details(selected_card):
                players_hand.remove(selected_card)
                last_played_cards.append(selected_card)
            else:
                players_hand.append(cards.pop(0))  # Player draws a card if invalid
            if selected_card.split('_')[1] == 'skip' or selected_card.split('_')[1] == 'reverse':
                if last_played_cards[-1].split('_')[0] == selected_card.split('_')[0]:
                    turn_to_play += 2
                else:
                    turn_to_play += 1
            elif selected_card.split('_')[1] == 'draw 2':
                turn_to_play += 1
                draw_2()
            elif selected_card.split('_')[1] == 'draw 4':
                turn_to_play += 1
                draw_4()
            elif selected_card.split('_')[1] == 'card':
                wild_color_card()
                turn_to_play += 1
                # last_played_cards.remove(selected_card)
            elif selected_card.split('_')[1] == 'draw 4':
                turn_to_play += 1
                draw_4()
                # last_played_cards.remove(selected_card)
            else:
                turn_to_play += 1

            break
        else:
            user_input = input(f'Invalid choice, pick a valid card (1-{len(players_hand)}): ')

# comp turn 
def comps_turn():
    global turn_to_play
    print("\nComp's turn!")
    print(f"Comp's hand: {comps_hand}")

    valid_card_found = False
    for comp_played_card in comps_hand:
        if get_top_card_details(comp_played_card):
            last_played_cards.append(comp_played_card)
            comps_hand.remove(comp_played_card)
            valid_card_found = True
            break  # Exit after playing the first valid card

    # print(f"Comp played: {comp_played_card}")
    if not valid_card_found:
        drawn_card = cards.pop(0)
        comps_hand.append(drawn_card)
        print(f"Comp draws a card: {drawn_card}")

    if comp_played_card.split('_')[1] == 'skip' or comp_played_card.split('_')[1] == 'reverse':
        turn_to_play += 2
    elif comp_played_card.split('_')[1] == 'draw 2':
        turn_to_play += 1
        draw_2()
    elif comp_played_card.split('_')[1] == 'draw 4':
        turn_to_play += 1
        draw_4()
    elif comp_played_card.split('_')[1] == 'card':
        wild_color_card()
        turn_to_play += 1
    else:
        turn_to_play += 1

def main():
    global first_card 
    first_card = 'red_0'
    last_played_cards.append(first_card)
    print(f'Starting card: {first_card}\n')

    while True:
        print(f'\n\tPlayed cards: {last_played_cards}\n')
        if turn_to_play % 2 == 0:
            comps_turn()
        else:
            players_turn()
        
        if len(players_hand) == 0:
            print("You win!")
            break
        elif len(comps_hand) == 0:
            print("Comp wins!")
            break

main()