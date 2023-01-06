#!/usr/bin/env python3.7


# define the ranks and suits of the cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['hearts', 'diamonds', 'clubs', 'spades']

# create a list of all the cards
cards = []
for suit in suits:
    for rank in ranks:
        cards.append(rank + ' of ' + suit)

# shuffle the cards
import random
random.shuffle(cards)

# deal the cards to the players
player1 = []
player2 = []
while len(cards) > 0:
    player1.append(cards.pop())
    player2.append(cards.pop())

# compare the hands to determine the winner
player1_score = 0
player2_score = 0

for card in player1:
    if 'A' in card:
        player1_score += 1
    elif 'K' in card:
        player1_score += 0.5

for card in player2:
    if 'A' in card:
        player2_score += 1
    elif 'K' in card:
        player2_score += 0.5

if player1_score > player2_score:
    print("Player 1 wins!")
elif player2_score > player1_score:
    print("Player 2 wins!")
else:
    print("It's a tie!")