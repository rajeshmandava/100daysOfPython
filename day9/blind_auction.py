
#HINT: You can call clear() to clear the output in the console.
import os
from art import logo

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

print(logo) 
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = -1;
  highest_bidder = ""
  for bidder in bidding_record:
    if highest_bid < bidding_record[bidder]:
      highest_bid = bidding_record[bidder]
      highest_bidder = bidder
  print(f"{highest_bidder} has won the blind auction at {highest_bid}")
      

while not bidding_finished:
  name = input("What is your name?")
  price = int(input("What is your bid?"))
  bids[name] = price
  should_continue = input("Are there any other bidder? Type 'Yes' or 'No'.")
  if should_continue == "No":
    bidding_finished = True
  elif should_continue == "Yes":
    cls()

find_highest_bidder(bids)

# cls()