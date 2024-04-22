# Blackjack by Oliver Peterson 2024

import random
from deck import spades, diamonds, hearts, clubs

print("\nWelcome to Blackjack.\nYour goal is to have a higher hand than the dealer, without going over 21.")

suits = [spades, diamonds, hearts, clubs]

money = 500

def face_check(card):
    '''Checks if a card is a face card, and adds the respective value'''
    face_cards = ["Jack", "Queen", "King"]
    if card in face_cards:
        card = 10
        return int(card)
    elif card == "Ace":
        if player_score < 11:
            card = 11
        else:
            card = 1
        return int(card)
    else:
        return int(card)

def draw_card():
    '''Randomly picks a suit, then picks a card from that suit.'''
    suit = random.choice(suits)  # picks a random suit from the deck
    card = random.choice(suit)  # picks a random card from the suit
    suit.remove(card)  # removes the card from the deck, for consistency
    return card

def check_win(player_total, dealer_total):
    '''Compares the player and dealer scores'''
    if player_total > dealer_total:
        print(f"\nYour score:     {player_score}")
        print(f"Dealer's score: {dealer_total}")
        print("\nYou win!\n")
        return [False, 0]
    elif player_total < dealer_total:
        print(f"\nYour score:     {player_score}")
        print(f"Dealer's score: {dealer_total}")
        print("\nYou lose.\n")
        return [False, 1]
    else:
        print(f"\nYour score:     {player_score}")
        print(f"Dealer's score: {dealer_total}")
        print("It is a tie.")
        return [False, 2]

playing = True
while playing:

    dealer_1 = draw_card()
    dealer_2 = draw_card()
    dealer_hand_full = [dealer_1, dealer_2]
    dealer_hand = dealer_hand_full

    # This is to check if the dealer has a face card. If they do, it will be converted into a numerical value.

    face_cards_dlr = {"Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
    if dealer_1 in face_cards_dlr:
        dealer_1 = face_cards_dlr[dealer_1]
    if dealer_2 in face_cards_dlr:
        dealer_2 = face_cards_dlr[dealer_2]

    dealer_score = int(dealer_1 + dealer_2)

    # Place your bets

    print(f"Money: ${money}")
    betting = True
    while betting:
        bet = input("How much would you like to bet? $")
        try:
            int(bet)
        except ValueError:
            print("Invalid input!")
        else:
            bet = int(bet)
            betting = False
    money = money - bet

    # Now, time for the player to draw cards.

    player_score = 0
    first_card = draw_card()
    second_card = draw_card()

    print(f"Dealer's cards are {dealer_1} and ???")
    print(f"\nYour cards are {first_card} and {second_card}.")

    # Adding scores.
 
    player_score += face_check(first_card)
    player_score += face_check(second_card)

    # At this point, the two cards have been drawn. Now, the player should draw cards until their total goes over 21.

    print(f"Your point total is {player_score}.\n")

    drawing = True
    while drawing:
        play = input(f"Would you like to draw another card? (Points: {player_score}) Y/N: ")
        if play.lower() == "n":
            results = check_win(player_score, dealer_score)
            # Here's where the money gets dealt out.
            if results[1] == 0:
                money += 2*bet
            elif results[1] == 1:
                money = money
            elif results[1] == 2:
                money += bet
            print(f"You now have ${money}")
            drawing = results[0]
        else:
            card = draw_card()
            print(f"You drew a {card}.")
            player_score += face_check(card)
            print(f"\nYour point total is: {player_score}.")
            if player_score > 21:
                print("Your score is over 21.\nYou lose.\n")
                drawing = False
            else:
                drawing = True
    cont = input("Would you like to play again? Y/N: ")
    if cont.lower() == "y":
        playing = True
    else:
        print(f"\nFinal Profit: ${money} - $500 = ${money - 500}")
        print("Thank you for playing!")
        playing = False

# Reading the code? Thanks for checking it out!