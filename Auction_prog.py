import artforAuction
import os
print(artforAuction.logo)
my_auction = {}
print("Welcome to the secret auction program.")
next_bid = "yes"
def auct_data():
    Name = input("What is your name?: ")
    Bid = input("What's your bid?: $")
    my_auction[Name] = Bid
while(next_bid == "yes"): 
            auct_data()
            next_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
            os.system('cls||clear')

winner = 0
for key in my_auction:
    winner = my_auction[key]
    if(my_auction[key] > winner):
        winner = my_auction[key]
print(f"The winner is {my_auction[winner]}, with Bid of ${winner}.")