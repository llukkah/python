print("Challenge 3.2: Playing with the stock market")

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# Write code to ask the client his name and save it to a variable.
name = str(input('What is your name?\n Your name '))

# Write code to ask the client his savings and save it to another variable.
savings = int(input('How much do you have in your savings?\n Your savings: '))

# Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? \nType\n 'amzn' for Amazon,\n 'aapl' for Apple,\n 'fb' for Facebook,\n 'goog' for Google\n 'msft' for Microsoft.\nYour answer: ")

# print("Challenge 3.2.2: Perform user-specific calculations")
# You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

# print("Challenge 3.2.3: Output for the user the result")


if stock == "amzn" and savings >= amazon:
        amazon_shares = savings / amazon
        yes_amazon = f'{name} has {savings} in savings and he can buy {amazon_shares} shares of {stock} at the current price of {amazon}'
        print(yes_amazon)
elif stock == "aapl" and savings >= apple:
        aapl_shares = savings / apple
        yes_apple = f'{name} has {savings} in savings and he can buy {aapl_shares} shares of {stock} at the current price of {apple}'
        print(yes_apple)
elif stock == "fb" and savings >= fb:
        fb_shares = savings / fb
        yes_fb = f'{name} has {savings} in savings and he can buy {fb_shares} shares of {stock} at the current price of {fb}'
        print(yes_fb)
elif stock == "goog" and savings >= google:
        goog_shares = savings / google
        yes_goog = f'{name} has {savings} in savings and he can buy {goog_shares} shares of {stock} at the current price of {google}'
        print(yes_goog)
elif stock == "msft" and savings >= msft:
        msft_shares = savings / msft
        yes_msft = f'{name} has {savings} in savings and he can buy {msft_shares} shares of {stock} at the current price of {msft}'
        print(yes_msft)
else:
        print('you do not have enough money in your savings to buy any shares.')
#########################################
#########################################
#########################################
#########################################
#########################################
#########################################
#########################################
# if stock == "amzn":
#     if savings >= amazon:
#         amazon_shares = savings / amazon
#         yes_amazon = f'{name} has {savings} in savings and he can buy {amazon_shares} shares of {stock} at the current price of {amazon}'
#         print(yes_amazon)
#     else:
#         print('you do not have enough money in your savings to buy 1 amazon share.')
# if stock == "aapl":
#     if savings >= apple:
#         aapl_shares = savings / apple
#         yes_apple = f'{name} has {savings} in savings and he can buy {aapl_shares} shares of {stock} at the current price of {apple}'
#         print(yes_apple)
#     else:
#         print('you do not have enough money in your savings to buy 1 apple share.')

# if stock == "fb":
#     if savings >= fb:
#         fb_shares = savings / fb
#         yes_fb = f'{name} has {savings} in savings and he can buy {fb_shares} shares of {stock} at the current price of {fb}'
#         print(yes_fb)
#     else:
#         print('you do not have enough money in your savings to buy 1 facebook share.')

# if stock == "goog":
#     if savings >= google:
#         goog_shares = savings / google
#         yes_goog = f'{name} has {savings} in savings and he can buy {goog_shares} shares of {stock} at the current price of {google}'
#         print(yes_goog)
#     else:
#         print('you do not have enough money in your savings to buy 1 google share.')

# if stock == "msft":
#     if savings >= msft:
#         msft_shares = savings / msft
#         yes_msft = f'{name} has {savings} in savings and he can buy {msft_shares} shares of {stock} at the current price of {msft}'
#         print(yes_msft)
#     else:
#         print('you do not have enough money in your savings to buy 1 microsoft share.')

#########################################





