from replit import clear
from art import logo

bids={}
bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the bid of ${highest_bid}")    
      

while not bidding_finished:
  name = input("what is your name?: ")
  price = int(input("what is your bidding price: $"))
  bids[name]= price
  should_continue = input("are there any other bidders 'yes or no'")
  if should_continue =="no":
    bidding_finished = True
    highest_bidder(bids)
  elif should_continue =="yes":
    clear()

  

    
  
#HINT: You can call clear() to clear the output in the console.
