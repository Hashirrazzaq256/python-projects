############### Blackjack Project #####################

import random
from replit import clear
from art import logo
def deal_card():
 cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 card =  random.choice(cards)
 return card 

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  game_over = False
  for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
      return 0 
    if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
      
    return sum(cards)
    
  
 
  while not game_over:
    user_result= calculate_score(user_cards)
    computer_result = calculate_score(computer_cards)
    print(f" your cards {user_cards} and your sum {user_result} ")
    print(f"computers cards = {computer_cards[0]}")
    
    if user_result==0 or computer_result == 0 or user_result>21:
      game_over =True
    else:  
        if input("do you want to draw another card press y for yes and n for pass ").lower() =="y":
         user_cards.append(deal_card())
        else:
         game_over = True  
  while computer_result !=0 and computer_result<17:
    computer_cards.append(deal_card())
    computer_result = calculate_score(computer_cards)
  def compare(user_result,computer_result):
    if user_result== computer_result:
      print("its a draw")
    elif computer_result==0:
      return "You Lost , Opponent has a blackjack"
    elif user_result ==0:
      return " You won You got a blackjack"
    elif user_result>21:
      return "you went over 21 you lost"
    elif computer_result>21:
      return "Computer went over you won"
    elif user_result >computer_result:
      return "You won"
    else:
      return "You lost computer won"    
  print(f"  your final cards: {user_cards}, and your final result {user_result}")
  print(f"  computer final cards: {computer_cards} and Computer's final result {computer_result}")
  print(compare(user_result,computer_result))
  
while input("Do you want to play  game ? type 'y' for yes and 'n' for no ").lower() =='y':
  clear() 
  play_game()

