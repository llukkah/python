
#####################################
#####################################
######## MANIPULATING DATA ##########
#####################################
#####################################
SLICE
    SYNTAX: slice(start, end, step)
            start - Optional. An integer number specifying at which position to start the slicing. Default is 0
            end	- An integer number specifying at which position to end the slicing
            step - Optional. An integer number specifying the step of the slicing. Default is 1
        EXAMPLE : 
            a = ("a", "b", "c", "d", "e", "f", "g", "h")      list of letters
            x = slice(3, 5)                                   Start the slice object at position 3, & slice to position 5
            print(a[x])                                       return the result
                                returns: ('d', 'e')

NOTE WITH INDEXES IN LISTS
        When counting Indexes in lists, it ALWAYS start at ZERO
                a = ("a", "b", "c", "d", "e", "f", "g", "h")
     index number =   0    1    2    3    4    5    6    7

When slicing, the END position will not be returned.  That is why the slice ends at 5.  If you wanted to include 5 in the return statement, change the END position to 6.

#####################################
#####################################
INDEX LOOK UP
    If you know the index number of the element you're trying to find, you can target it by adding [index number] to the end of your list variable
    EXAMPLE :
        hello_world = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
        print(hello_world[0])
            returns: h

To find the index number of an element use the index method:
    SYNTAX: list.index(obj)
    aList = [123, 'xyz', 'zara', 'abc']
    print (aList.index('xyz'))
                Returns: 1
#####################################
#####################################
REMOVE -  removes the specified item.
    SYNTAX: list.remove("item to be removed")
    EXAMPLE:
        thislist = ["apple", "banana", "cherry"]
        thislist.remove("banana")
        print(thislist)
                RETURNS: thislist = ["apple", "cherry"]

POP - removes the specified index.
    SYNTAX: list.pop(1)
        If you do not specify the index, the pop() method removes the last item.
    EXAMPLE:
        thislist = ["apple", "banana", "cherry"]
        thislist.pop(1)
        print(thislist)
                RETURNS: thislist = ["apple", "cherry"]
#####################################
#####################################
SPLIT - splits a string into a list.
    SYNTAX - string.split(separator, maxsplit)
        separator - Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
        maxsplit - Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
                    When maxsplit is specified, the list will contain the specified number of elements plus one.
    EXAMPLE:
        txt = "hello, my name is Peter, I am 26 years old"      text to be split
        x = txt.split(",")                                     splitting the string by commas(,) and saving it to a variable
        print(x)                                                returning the split results
                        RETURN: ['hello', 'my name is Peter', 'I am 26 years old']
#####################################
#####################################
APPEND - adds an element to the end of the list.
    SYNTAX: list.append(elmnt)
        elmnt - Required. An element of any type (string, number, object etc.)
    EXAMPLE: 
        fruits = ['apple', 'banana', 'cherry']
        fruits.append("orange")
            RETURNS: ['apple', 'banana', 'cherry', 'orange']
######################################
######################################
JOIN - takes all items in an iterable and joins them into one string.
    A string must be specified as the separator.
        SYNTAX: string.join(iterable)
            iterable - Required. Any iterable object where all the returned values are strings
######################################
######################################
REPLACE data in a string
    words =["hello", "world", "how", "are", "you?"]
    words[2] = "no way"
        Returns: words =["hello", "world", "no way", "are", "you?"]
