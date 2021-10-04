#####################################
#####################################
##### LISTS INSIDE A DICTIONARY #####
#####################################
#####################################
cart = {
    'fruits': ['mangoes', 'pears', 'apples'],
    'vegetables':['spinach', 'peas'],
    'price': 32.21
}
#####################################
GET list inside a dictionary
    print(cart['vegetables'])   #returns whole list
    print(cart['vegetables'][0])    #returns specific element in list
#####################################
ADD 
#####################################
UPDATE elements inside list
    cart['vegetables'][0] = 'papayas'
#####################################
DELETE



#####################################
#####################################
##### DICTIONARIES INSIDE A #########
########## DICTIONARY ###############
#####################################
restaurants = {
    'El Basurero': {
        'address': '32-17 Steinway St, Queens, NY 11103',
        'menu_url': 'https://www.allmenus.com/ny/astoria/366154-el-basurero/menu/'
    },
    'SriPraPhai': {
        'address': '64-13 39th Ave, Woodside, NY 11377',
        'menu_url': 'https://sripraphai.com/menu.html'
    }
}
#####################################
GET specific dictionary inside a dictionary
    print(restaurants['SriPraPhai'])
#####################################
ADD dictionary to dictionary
    restaurants['Joes Pizza'] = {'address': '123 main street',
                                  'phone number': '1234567'}
#####################################
UPDATE items in nested dictionary
    restaurants['Joes Pizza']['menu_url'] = 'google.com'
#####################################
DELETE item in nested dictionary
    restaurants['Joes Pizza'].pop('phone_number')


#####################################
#####################################
##### DICTIONARIES INSIDE A LIST ####
#####################################
#####################################
users = [
    {'username': 'alanna', 'password': 'javascript', 'last_login': '9/28/2020'},
    {'username': 'aryn', 'password': 'dictionaries'},
    {'username': 'yusuf', 'password': 'django', 'last_login': '9/26/2020'},
    {'username': 'paul', 'password': 'github'}
]
#####################################
GET specific dictionary inside a LIST
    print(users[2])
#####################################
GET specific info from dictionary inside a LIST
    print(users[2]['password'])
#####################################
ADD dictionary to a list
    users.append({'username': 'serena', 'password': 'java'})
#####################################
UPDATE dictionary nested in list
    users[1]['verified_account'] = True     #adding new key: value pair to specific user
    users[1]['password'] = 'helloworld'     #updating existing data in dictionary
#####################################
REMOVE info from dictionary
    users[0].pop('last_login')

#####################################
#####################################
######### LIST INSIDE A LIST ########
#####################################
#####################################
shopping_list = [['mangoes', 'apples', 'oranges'],
                  ['carrots', 'brocoli'],
                  ['corn flakes', 'oatmeal']]
#####################################
ACCESS specific list
    print(shopping_list[0]) #get first list
    print(shopping_list[0][1]) #get first list, and second item in that list
#####################################
UPDATE items in list
    shopping_list[0][1] = 'beets'   #replacing apples for beets
#####################################
ADD list/items in a list
    shopping_list.append(['milk', 'eggs'])
    shopping_list[0].append('grapes')   # adds grapes to end of list
#####################################
DELETE item in a list
    shopping_list[1].remove('broccoli')