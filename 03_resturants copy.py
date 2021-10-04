print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 
Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

# print(restaurant)

print('latitude and longitude of Four Barrel Coffee:')
longitude = restaurant.get("longitude")
lat = restaurant.get("latitude")
print(longitude)
print(lat)

print('complete address of the Four Barrel Coffee, formatted as a string:')
street = restaurant.get('address1')
city = restaurant.get('city')
state = restaurant.get('state')
zip = restaurant.get('zip_code')
print(street + " " + city + " " + state + " " + zip)

print('URL of the website of Four Barrel Coffee:')
url = restaurant.get('url')
print(url)

print()
print("Question 2")

print('Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them')
#  with the following key-value pairs:
# #         1. name : name of the resturant (string)
# #         2. address: address of the restaurant (string)
# #         3. favourite_dish: your favourite thing to order at the restaurant (string)

restaurant1 = {
    "name": "Bodega",
    "address": "any street corner, new york, ny 10001",
    "favorite_dishes": "chopped cheese"
}
restaurant2 = {
    "name": "bareburger",
    "address": "123 main street brooklyn ny 11705",
    "favorite_dishes": "chicken fingers"
}
restaurant3 = {
    "name": "champion",
    "addressurl": "100 delancy street new york, ny 11725",
    "favorite_dishes": "dollar slice"
}
print('Print each dictionary')
print(restaurant1)
print(restaurant2)
print(restaurant3)

# # The dictionary for each restaurant should look something like this

# '''
# restaurant_1  = {
#     "name": "Subway",
#     "address" : "116th & Broadway, NY 10016",
#     "favourite_dish" : "Chicken BLT Sandwich" }
# '''

print()

print("Question 3")
# '''
# Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
# Remove the 'favourite_dish' key value pair from that restaurant's dictionary
# '''

print('Remove the favorite_dish key-value pair from one of your 3 restaurants')
print('Print the new dictionary.')
restaurant1.pop("favorite_dishes")
restaurant2.pop("favorite_dishes")
restaurant3.pop("favorite_dishes")
print(restaurant1)
print(restaurant2)
print(restaurant3)
print()

print("Question 4")
# '''
# Imagine that another one of your most favourite restaurants modified its address. 
# Update just this value in that restaurant's dictionary
# '''

print('Update the address field of 1 restaurant')
print('Print the new address of the restaurant')
print('Print the updated dictionary.')
restaurant1["address"]= '1234 beach avenue'
new_address = restaurant1.get("address")
print(new_address)
print(restaurant1)
# print()