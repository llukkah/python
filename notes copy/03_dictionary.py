
######################################
######################################
############ DICTIONARY ##############
######################################
######################################
EXAMPLE: thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964,
      "tires": [4, 2]
    }
######################################
######################################
ACCESS the items of a dictionary:
    -By referring to its key name, inside square brackets:
        x = thisdict["model"]
    -GET Method: 
        SYNTAX : x = thisdict.get("key")
    -accessing when Value is a LIST
        print(thisdict['tires'][0])


######################################
######################################
REMOVING Items from dictionary

POP - removes the item with the specified key name:
    thisdict.pop("model")
    print(thisdict)

DEL - removes the item with the specified key name:
        del thisdict["model"]
        print(thisdict)
    can also delete the dictionary completely
        del thisdict


######################################
######################################
Update items from dictionary - 2 ways
    - Update method - 
        SYNTAX - thisdict.update({"key":value})
            EXAMPLE: Update the "year" of the car by using the update() method:
            thisdict.update({"year": 2020})
    - Change the value of a specific item by referring to its key name
            thisdict["year"] = 2018


######################################
######################################
ADDING new key:value pairs to dictionary
    thisdict["mileage"] = "12345 miles"

    
######################################
######################################
ADDING new items in a list of a key:value pair
    thisdict["tires"].append(3)