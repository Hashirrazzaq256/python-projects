import random
from art import logo,vs
from game_data import data

print(logo)
account_a = random.choice(data)
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
def check_answer(guess,a_followers,b_followers):
  
guess = input("who has more followers ?").lower()


a_followers = account_a["follower_count"]
b_followers = account_b["follower_count"]
