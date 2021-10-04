
######################################
######################################
###### Conditional Statements ########
######################################
######################################
    Statements that are only executed if the conditional expression is met.

    IF/ELIF/ELSE code Blocks: 
    		if CONDITION no. 1:                         AKA : If this condition no 1. is True:
               code block no. 1                                   run code block no.1.
            elif CONDITION no.2:                            elif condition no.1 is False, and condition no. 2 is True:
                code block no.2                                   run code block no.2
            else:                                           else all the conditions listed above are False:
               code block no. 3                                   run code block no. 3

        EXAMPLE:
    		if strawberry_stock > 0:
    		    print("I'm buying strawberry ice cream")
    		else:
    		    print("I'm buying chocolate ice cream")
    -OR-
    		if strawberry_stock > 0:
    		    print("I'm buying strawbery ice cream")
    		elif chocolate_stock > 0:
    		    print("I'm buying chocolate ice cream")
    		else:
    	    print("I'm buying vanilla ice cream.”)

        CONDITION is a Boolean expression - True or False
######################################
######################################
COMBINING 2 CONDITION STATEMENTS
    AND  - run this code block if BOTH of the statements are True
        a = 200
        b = 33
        c = 500
        if a > b and c > a:
            print("Both conditions are True")

    OR - run this code block if EITHER of these statements are True:
        a = 200
        b = 33
        c = 500
        if a > b or a > c:
            print("At least one of the conditions is True")
    NOT - Reverse the result, returns False if the result is true.
        x = 5
        print(not(x > 3 and x < 10))
                Returns: False

    NESTED IF STATEMENTS - if statements inside if statements
        x = 41
        if x > 10:
            print("Above ten,")
            if x > 20:
                print("and also above 20!")
        else:
            print("but not above 20.")
######################################
######################################
###### Comparison Operators ##########
######################################
######################################
 	All 6 comparison operators and the condition under which each will return True:		
         x == y               # x is equal to y		
         x != y               # x is not equal to y		
         x > y                # x is greater than y		
         x < y                # x is less than y		
         x >= y               # x is greater than or equal to y		
         x <= y               # x is less than or equal to y
