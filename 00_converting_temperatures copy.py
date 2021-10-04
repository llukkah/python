# The formula for converting between fahrenheit and celsius is to first subtract 32, then multiply by 5/9. Can you do the following in python?

# Convert a temperature of 100 degrees fahrenheit to celsius
# Save this to a variable called celsius_100, and use print() to print out the value
celsius_100 = (100-32)*(5/9)
print(celsius_100)

# Is the resulting temperature you get an integer or float? How do you know?
#it is a float
print(type(celsius_100))

# Convert a temperature of 0 degrees fahrenheit to celsius
# Save this to a variable called celsius_0, and use print() to print out the value
celsius_0 = (0-32)*(5/9)
print(celsius_0)

# Convert a temperature of 34.2 degrees fahrenheit to celsius
# Do this one all in one print statement without saving any variables
print((34.2-32)*(5/9))

# Convert a temperature of 5 degrees celsius to fahrenheit?
# multiply 9/5 and add 32.
celsius_5 = ((5*1.8) + 32)
print(celsius_5)
# What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
celsius_302 = ((30.2*1.8) + 32)
print(celsius_302)
#30.2 C is hotter

