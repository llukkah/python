# -*- coding: utf-8 -*-
# 3-point shots
# 1 Jamal Murray - 46
# 2 Fred VanVleet - 43
# 3 James Harden rank - 37

#3-point shot attempts
# Jamal Murray - 93
# Fred VanVleet - 110 
# James Harden - 109

print('Challenge 2.1: Store the number of three point shots made in variables for each player')
jamal_score = 46
fred_score = 43
james_score = 37

# Challenge 2.2: Print out the number of three point shots using f-strings with the variables created for each player in 2.1
# Note: Make sure to use the variables you created in Challenge 2.1 in the print statements!
print('Challenge 2.2: Print out the number of three point shots using f-strings with the variables created for each player in 2.1')
jamal = f'jamal score is {jamal_score}'
print(jamal)
fred = f'fred score is {fred_score}'
print(fred)
james = f'jamal score is {james_score}'
print(james)

print('Challenge 2.3: Store the number of three point shot attempts in variables for each player')
jamal_shot_attempt = 93
fred_shot_attempt = 110
james_shot_attempt = 109

print('Challenge 2.4: Build on your print statement!')
jamal_total = f'jamal 3 point score is {jamal_score} and shot attempts is {jamal_shot_attempt}'
print(jamal_total)
fred_total = f'fred 3 point score is {fred_score} and shot attempts is {fred_shot_attempt}'
print(fred_total)
james_total = f'james 3 point score is {james_score} and shot attempts is {james_shot_attempt}'

print('Challenge 2.5: Calculate and print the three point percentage for each player')
jamal_3_percent = jamal_score / jamal_shot_attempt
print(jamal_3_percent)
fred_3_percent = fred_score / fred_shot_attempt
print(fred_3_percent)
james_3_percent = james_score / james_shot_attempt
print(james_3_percent)

print('Challenge 3.1 Print out the paragraph but with only 1 sentence per line')
print('The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \mThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. They were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.')

print('Challenge 3.2 Print out the paragraph with only 1 sentence per line, and all in upper case')
para = 'The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \mThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. They were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.'
print(para.upper())

print('Challenge 3.3 Are the Lakers the best team?')
lakers_are_best = True
lakers = f'it is {lakers_are_best} that The lakers are the best basketball team in the NBA'
print(lakers)

print('Challenge 3.4 Type conversion')
print('Convert your lakers_are_best variable to an integer, and print it out.Why do you think it takes this value?')
lakers_int = int(lakers_are_best)
print(lakers_int)
#takes this value because booleans are represented as a 1 or 0.
print('Convert your lakers_are best variable to a float, and print it out')
lakers_float = float(lakers_int)
print(lakers_float)

print('Challenge 3.5 Type conversion part 2')
print('Take each players three point percentage from part 2.5 and convert it to a string, then print it out. What do you notice?')
jamal_string = str(jamal_3_percent)
fred_string = str(fred_3_percent)
james_string = str(james_3_percent)

print(jamal_string)
print(fred_string)
print(james_string)
print(type(jamal_string))
# it prints as the same average, however it is now a string.
print('Take each players three point percentage from part 2.5 and convert it to an integer, then print it out. What do you notice here?')

jamal_int = int(jamal_3_percent)
fred_int = int(fred_3_percent)
james_int = int(james_3_percent)

print(jamal_int)
print(fred_int)
print(james_int)
print(type(jamal_int))
#the integer it gives back is zero because it cuts everythign to the right of the decimal out. and changes it to an int.