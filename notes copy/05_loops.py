
######################################
######################################
############## WHILE LOOPS ###########
######################################
######################################
While Loop - keep looping while a condition is true
        EXAMPLE: 
      	while number <= 100 print(‘hello’)
      	    -This would be an example of what is called indefinite iteration, 
               meaning we don't know how many times we'll need to perform the loop body. 


######################################



######################################
######################################
############## FOR LOOPS #############
######################################
######################################

For Loop - allows us to repeat a task a specific number of times, and to use different data (such as a different name) each time we repeat.
        EXAMPLE: 
          	coworker_names = ["Mike", "Jessica", "Sheila", "Anton", "Kim"] 
       		for name in coworker_names:     
      	    print("Good morning, " + name + "!")

          -The first line of the loop specifies a list of names.
          -The code within the loop will execute once for each item in the list, with the value of the name 
              variable being updated to have the value of each item in the list, in turn. 
          -If there are 10 items in the list, the loops repeats 10 times.
          -The variable name can be given any other name that we like.

This is called definite iteration - have a definite (fixed, defined) number of times that we will perform the loop body.


######################################
Looping through a string 
    EXAMPLE:
        mystring = 'hello_world'
        vowels = ['a', 'e', 'i', 'o', 'u']
        for letter in mystring:
            if letter in vowels:
                print('yes')
            else:
                print('no')


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