print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
for i in range(len(meats)):
    meats[i] = meats[i].capitalize()

for i in range(len(cheeses)):
    cheeses[i] = cheeses[i].capitalize()

# print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []
for meat in meats:
    for cheese in cheeses:
        sandwiches.append(f'{meat} and {cheese}')

print(sandwiches)

print()


# print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'
cust_order = (input("What sandwhich would you like?  \nType:\nHam and Cheddar\nHam and Swiss\nHam and Pepper jack\nHam and Provolone\nTurkey and Cheddar\nTurkey and Swiss\nTurkey and Pepper jack\nTurkey and Provolone\nChicken and Cheddar\nChicken and Swiss\nChicken and Pepper jack\nChicken and Provolone\nTuna and Cheddar\nTuna and Swiss\nTuna and Pepper jack\nTuna and Provolone\n\nYour Choice: "))

for sandwich in sandwiches:
    if cust_order == sandwich:
        print(f'Great choice! 1 {cust_order} coming right up!')
        break