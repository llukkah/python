# define a class
###############################
###############################
##### CREATING A CLASS ########
###############################
###############################
class Person(): #this is setting up the class of a person
# next to initialize the class by the initinalization class 
    def __init__(self, name, age):
        #this initilization function sets up attributes of the class we're setting up.
        # self - something to always pass in the initilization function to refer to itself(class).  self refers to the object you originally created
        self.name = str(name)
        self.age = age
#only need to init 1 time, but can make many people as much as you want.. line 15 and line 26
    def greeting(self)
        return f'hello {self.name}'

person = Person("llukkah, 31")
# person - self.name
# llukkah = name on line 4
# Person - className (Person)

###############################
###############################
###### CLASS METHODS ##########
###############################
###############################

person2 = Person("claire")

#syntax - 
# object.method()

###############################
###############################
###### Add info to Class ######
###### DYNAMIC EDIT ###########
###############################
class Cart():
    def __init__(self):
        self.items = []
    
    def add (self, name, price):
        item = {}
        item['name'] = name
        item['price'] = price
        self.items.append(item)

cart = Cart()
cart.add("oreos", 12)
cart.add("pasta", 5)

print(cart.items)

###############################
###############################
###### Looping in a Class #####
###############################
###############################
#find total amount in your cart
class Cart():
    def __init__(self):
        self.items = []
    
    def add (self, name, price):
        item = {}
        item['name'] = name
        item['price'] = price
        self.items.append(item)
    
    def total(self):
        cart_total = 0
        for item in self.items:
            cart_total += item['price']
        return f'${cart_total}'

print(cart.total())

###############################
###############################
###### Atributes outside INIT##
###############################
###############################
#name and age is something user sets, but if you want to set a GLOBAL VARIABLE for all users:

class Person():
    role = 'teacher'  #by doing this, every person we create will be a teacher
    #set up global variable before init function
    def __init__(self, name, age):
        self.name = str(name)
        self.age = age
    def greeting(self)
        return f'hello {self.name}'

print(person.role)