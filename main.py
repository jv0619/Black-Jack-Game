############### Blackjack Project #####################

from random import choice
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card(s_cards):
  """ It returns a card from cards list"""
    card = [choice(s_cards)]
    return card
wanna_play = True if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y' else False
while (wanna_play):
  print(logo)
  player_cards = [] + pick_card(cards) + pick_card(cards)
  dealer_cards = [] + pick_card(cards) + pick_card(cards)
  p_score = sum(player_cards)
  c_score = sum(dealer_cards)
  print(f"Your cards: {player_cards}, current score: {p_score} \n Computer's first card:{dealer_cards[0]}")
  is_taking_another = True if (input("Type 'y' to get another card, type 'n' to pass:") == 'y') else False
  while (is_taking_another and p_score < 21):
    player_cards += pick_card(cards)
    p_score = sum(player_cards)
    if p_score > 21 and player_cards[-1] == 11:
      player_cards[-1] = 1
      p_score -= 10
    if (p_score < 21):
      print(f"Your cards: {player_cards}, current score:{sum(player_cards)} \n Computer's first card: {dealer_cards[0]}")
      is_taking_another = True if input("Type 'y' to get another card, type 'n' to pass:") == 'y' else False
  while (c_score < 17):
    dealer_cards += pick_card(cards)
    c_score = sum(dealer_cards)
    if(c_score < 21 and dealer_cards[-1] == 11):
      dealer_cards[-1] = 1
      c_score -= 10
  print(f" Your final hand: {player_cards}, final score: {p_score}")
  print(f" Computer's final hand: {dealer_cards}, final score: {c_score}")
  if (p_score > 21):
    print('You went over. You lose \U0001F624')
  elif (c_score > 21):
    print('Opponent went over. You win \U0001F601')
  elif (c_score < p_score):
    print('You win \U0001F604')
  elif(c_score > p_score):
    print('Computer Win \U0001F62D')
  else:
    print('Draw... \U0001F642')
  wanna_play = True if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y' else False
  clear()