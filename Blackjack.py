# Blackjack! Some of the code might be a bit bulky, I couldn't get some parts to work as condensed functions, but here it is.

import random
from deck import spades, diamonds, hearts, clubs, face_cards

# Face cards

print("\nWelcome to Blackjack.\nYour goal is to have a higher hand than the dealer, without going over 21.")

streak = 0

playing = True
while playing:
    suits = [spades, diamonds, hearts, clubs]

    def face_check(dealer_card):
        face_cards_dlr = {"Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
        if dealer_card in face_cards_dlr:
            return face_cards_dlr[dealer_card]

    def draw_card():
        '''Randomly picks a suit, then picks a card from that suit.'''
        suit = random.choice(suits)  # picks a random suit from the deck
        card = random.choice(suit)  # picks a random card from the suit
        suit.remove(card)  # removes the card from the deck, for consistency
        return card

    dealer_1 = draw_card()
    dealer_2 = draw_card()
    dealer_hand_full = [dealer_1, dealer_2]
    dealer_hand = dealer_hand_full
    # This was during the initial process, to make sure the dealer had the right amount of points for his cards.
    # print(f"The Dealer has {dealer_1} and {dealer_2} in his hand.")

    # This is to check if the dealer drew a face card. If he did, it will be converted into a numerical value.

    face_check(dealer_1)
    print(dealer_1)
    face_check(dealer_2)
    print(dealer_2)

    dealer_total = int(dealer_1) + int(dealer_2)

    # Now, it's time for the player to draw cards!

    card_list = []
    player_score = 0
    first_card = draw_card()
    card_list.append(first_card)
    second_card = draw_card()
    card_list.append(second_card)

    print(f"\nYour cards are {first_card} and {second_card}.")

    # Adding scores.
    # Couldn't figure out how to work this into a function, I'll leave that for later.

    if first_card in face_cards:
        first_card = 10
        player_score += 10
    elif first_card == "Ace":
        if player_score < 11:
            first_card = 11
        else:
            first_card = 1
        player_score += first_card
    else:
        player_score += first_card

    if second_card in face_cards:
        second_card = 10
        player_score += 10
    elif second_card == "Ace":
        if player_score < 11:
            second_card = 11
        else:
            second_card = 1
        player_score += second_card
    else:
        player_score += second_card

    # At this point, the two cards have been drawn. Now, the player should draw cards until their total goes over 21.

    print(f"Your point total is {player_score}.\n")

    drawing = True
    while drawing:
        play = input(f"Would you like to draw another card? (Points: {player_score}) Y/N: ")
        if play.lower() == "n":
            if player_score > dealer_total:
                print(f"\nYour score:     {player_score}")
                print(f"Dealer's score: {dealer_total}")
                print("\nYou win!\n")
                streak += 1
                drawing = False
            elif player_score < dealer_total:
                print(f"\nYour score:     {player_score}")
                print(f"Dealer's score: {dealer_total}")
                print("\nYou lose.\n")
                streak = 0
            drawing = False
        else:
            card = draw_card()
            print(f"You drew a {card}.")
            if card in face_cards:
                card = 10
                player_score += 10
            elif card == "Ace":
                if player_score < 11:
                    card = 11
                else:
                    card = 1
                player_score += card
            else:
                player_score += card
            print(f"\nYour point total is: {player_score}.")
            if player_score > 21:
                print("Your score is over 21.\nYou lose.\n")
                streak = 0
                drawing = False
            else:
                drawing = True
    print(f"Current win streak: {streak}")
    cont = input("Would you like to play again? Y/N: ")
    if cont.lower() == "y":
        playing = True
    else:
        print("Thank you for playing!")
        playing = False

# Reading the code, eh? Thanks for checking it out!