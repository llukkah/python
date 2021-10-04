######################################
######################################
############## Data Types ############
######################################
######################################
    -	Booleans - True, False
    - Integers - 1, 2, 3		
        Can be Positive, Negative and Zero	
    - Floats - 1.0, 1.5, 10.38
        If you have a float in a mathematical equation, a float will always be returned
    - Strings - “Hello 2 Students” “Cat” “What?”		 
        Escape Characters
            Line Break - \n
                -if you have a long string and want to break it up when it prints	
            Tab Indentation	- \t
                -each \t will create a tabbed line
        F Strings - variable = f'this is an {example} of an f string'
            -create strings using other variables
                EXAMPLE:
                    profit = 120
                    my_f_string = f‘The profit today is {profit}’
                    print(my_f_string)
                    
                ALSO- you can do math in the curlys
                    print(f ‘If i earn 200 and my expenses are 40, then my profit is $ {200 - 40}
        Concatenation - combine 2 strings together
            first - ‘diana’
            last = ‘rey’
            print (first + ‘’ + last)
        Upper and Lower Cases - .upper() // .lower()
            fullname = ‘Diana Rey’
            print(fullname.upper())
            print(fullname.lower())
######################################
######################################
##### Type Conversions Functions #####
######################################
######################################
     Type Conversion Functions - convert a value from one data type to another.
    
    int(variable, object etc) - take a float or a string and turn it into an integer.	
        NOTE: it does this not by rounding, but by truncating--it drops off all the numbers after the decimal. 
    float(variable, object etc) - take an integer or a string and turn it into a float.
    str(variable, object, etc) - take a float or an integer and turn it into a string. 
    type(object) // type(name, bases, dict,variable) - will tell you its data type

######################################
######################################
############ MATHEMATICS #############
######################################
######################################
Operators - are used to manipulate data. 	
        =  equal	
        + addition	
        / division and always results in a float
        - subtraction
        * multiplication	
        ** which performs exponentiation	
        % which is the modulus (or remainder) operator	

    Python will run the Operators according to PEMDAS
        parentheses
        exponents
        multiplication
        division
        addition
        subtraction

Concatenation -  combining strings together. When we concatenate strings, we form a new string that is a collection of both strings' characters.

input() - prints the string (in this case, it's called a prompt string) that we put in parentheses out to the shell so the user can read it.
		number = int(input("Enter the starting number: "))
		end_number = number + 9
		while number <= end_number:
 		   print(number)
	    number = number + 1
######################################
######################################
Range - 
  SYNTAX: range(start, stop, step)
        start - what number to start
        stop - what number to stop
        step - how many numbers to increment by
            EXAMPLE:
1        		max_number = input("Print all positive even numbers less than:")
2       		max_number = int(max_number)
3 	        	for number in range(0, max_number, 2):
4 	       	    print(number) 
                    1 we're asking user to input a number for us that will be our STOP NUMBER
                    2. we're saving that number to a variable and converting it into an integer
                    3. we're looping  through the number variable to find all the numbers from zero to the Max_number variable in increment
                        of 2.
                    4. We're printing each number within that range
######################################
######################################
Rounding - 
    SYNTAX : round(number, digits)
            number - the number you want rounded
            digits, how many decimal places you want it rounded to
         EXAMPLE : 
            x = round(5.76543, 3)
            print(x)
######################################
######################################
Average - 
		numbers = [2, 4, 6, 8]                  # list of numbers
		number_items = len(numbers)             # get number of items in the numbers variable
		sum_of_numbers = 0                      # set another variable to manipulate and add numbers to
		for number in numbers:                  # loop through the list adding up all the numbers
	     sum_of_numbers += number               # for each number found in NUMBERS variable, add it to sum_of_numbers
		 average = sum_of_numbers / number_items# get average

len - gives us the number of items in a string, list, dictionary or any iterable data type
    SYNTAX: len(object)
