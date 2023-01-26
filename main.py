from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the Secret Auction Program!")

bids = {}

continue_bidding = True

def winning_bid(bid_records):
  highest_bid = 0
  highest_bidder = ""
  
  for key, value in bid_records.items():
    highest_value = int(value)
    if highest_value > highest_bid:
      highest_bid = highest_value
      highest_bidder = key
  
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")

while continue_bidding:
  name = input("What is your name? ")
  bid = input("What is your bid? $")
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")
  
  bids[name] = bid
  if other_bidders == 'no':
    continue_bidding = False
    clear()
    winning_bid(bids)
  elif other_bidders == 'yes':
    clear()

