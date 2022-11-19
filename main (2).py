import random
from art import logo,vs
from game_data import data
from replit import clear
print(logo)
score = 0
game_play = True
account_b = random.choice(data)
while game_play:
  account_a = account_b
  account_b = random.choice(data)
 
  if account_a == account_b:
    account_b = random.choice(data)
  def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country =account["country"]
    return (f"{account_name} , a {account_description}, from {account_country}")
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")
  
    
  def get_random_account():
    """Get data from random account"""
    return random.choice(data)
  
  def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"
  def check_answer(guess,a_follower,b_follower):
    if a_follower > b_follower:
      return guess=='a'
    else:
      return guess=='b'
  guess = input("who has more followers ?").lower()
  
  
  a_followers = account_a["follower_count"]
  b_followers = account_b["follower_count"]
  
  is_correct= check_answer(guess,a_followers,b_followers)
  clear()
  print(logo)
  if is_correct:
    score +=1
    print(f"You are right, your score is {score}")
  else:
    game_play = False
    print(f"Sorry thats wrong , Final score {score}")
    

