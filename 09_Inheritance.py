Inheritance - A child class takes on methods and attributes from Parent class.  Takes on features of Parent class and have alterations and modifications, build and have new methods/attributes.

Can have multiple child classes and 1 Parent.

Parent Class (Super Class)
    \
     \ (inherits/extends)
     Child Class (Sub Class)


     EXAMPLE
      Account Type  (Parent)
      /  |      \
    /    |       \
Guest   Admin  Standard     



Polymorphism - Overriding
    -Child class can override methods of a parent class

    Animal (Parent) - has 2 methods - move() and eat()
    |
    |
    Dog - has 2 functions move() and bark()
            this move() method overrides Animal's move() method

###################################
###################################
####### Creating Parent Class #####
###################################
###################################
class Account():
    def __init__(self, username):
        self.username = username

    def display_info(self):
        print(f'Account for user: {self.username}')


account1 = Account(username = 'llukkah')
account1.display_info()

###################################
###################################
####### Creating CHILD Class ######
###################################
###################################
class Guest(Account):   # put Parent class inside () to make it a child of the Account class

account2 = Guest(username='llukkah')
account2.display_info()

###################################
###################################
### Initializing CHILD Class ######
###### with attributes ############
###################################
class Guest(Account):
    def __init__(self, username, email): #username, just like in parent class, email is an attribute to the Guest class
        Account.__init__(self, username) # initializing Parent Class inside init method of Child class.
        self.email = email

account3 = Guest(username="llukkah")
#if you run this, it will give you and error because email is missing.  must initialize w all atributes
print(account2.email)

###################################
###### Using Super ()  to #########
### initialize a Child Class ######
###################################
###################################
class Guest(Account):
    def __init__(self, username, email):
        super().__init__(self, username) # super will run init method for whatever the parent class is.  In this case it's Account.  same as line 61 - Account.__init__(self, username)
        self.email = email

account3 = Guest(username="llukkah", email = "hey@email.com")
print(account2.email)

Super() / Super Class - always means parent class that's inside the () of the child class.  You can now use Super instead of Account / parent class name.

###################################
###################################
####### Adding Methods to #########
############ Child Class ##########
###################################
class StandardUser(Account):
    def __init__(self, username, password):
        super().__init__(username)
        self.password = password
    
    def login(self):
        password_attempt = input('Please enter your password: ')
        if password_attempt = self.password:
            print('Logged in!')
        else:
            print('Incorrect password!')

account3 = StandardUser(username = "llukkah", password = "123")
account3.login()

###################################
############ POLYMORPHISM #########
####### Overriding Methods in #####
############ Child Class ##########
###################################
class StandardUser(Account):
    # def __init__(self, username, password):
    #     super().__init__(username)
    #     self.password = password
    
    # def login(self):
    #     password_attempt = input('Please enter your password: ')
    #     if password_attempt = self.password:
    #         print('Logged in!')
    #     else:
    #         print('Incorrect password!')
    def display_info(self):
        print(f'Account for user: {self.username}')
        print('this accound is password-protected')

    # ^^ to override the display_info method in Account class (line 37), just redefine the method in the child class 

###################################
# doing more polymorphism 
###################################
class Guest(Account):
    # def __init__(self, username, email):
    #     Account.__init__(self, username)
    #     self.email = email

    def display_info(self):
        print(f'Account for user: {self.username} with email address: {self.email}')

print(type(account1))
account1.display_info()
#<class '__main__'.Account'>
# Account for user: llukkah
print(type(account2))
account2.display_info()
#<class '__main__'.Guest'>
#Account for user: llukkah with email address hey@email.com
print(type(account3))
account3.display_info()
#<class '__main__'.Standard User'>
# Account for user: llukkah
# This account is password protected

###################################
###################################
####### MULTIPLE INHERITANCE ######
###################################
###################################
class TwitterUser():
    def __init__(self, handle):
        self.handle = handle


class TwitterAccount(StandardUser, TwitterUser): #inheriting from 2 parents
#twitterAcocunt will have both attributes from both standard and twitter user.
    def __init__(self, username, password, handle): # list all attributes of parents
    #initialize both parent classes
        StandardUser.__init__(self, username, password)
        TwitterUser.__init__(self, handle)
    
    def display_info(self): #overriding display_info method of parent
    #handle is inheriting from parent class of TwitterUser
    #username inheriting from Standard User/from parent Account class
        print(f'Account for user: {self.username}n\ handle: {self.handle}')
        print('this account is password protected')

account4 = TwitterAccount(username="alex", password="1234", handle="@alex")
account4.display_info()

###################################
###################################
####### Importing Classes from ####
########## Seperate File ##########
###################################
from fileName import *