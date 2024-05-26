users = {
    123: "@aditya",
    124:"@aman",
    125: "@aniket"
}

# adding item
users[126] = "@rupesh"

users.pop(125) # it will returns the value corresponding to the key

users.popitem() # it will returns the key value pair of last item

# iterator will returns the key
for item in users:
    print(users[item])

# iterator will returns the values

for item in users.values():
    print(item)

# iterator will returns the tuple of key and value
for x,y in users.items():
    print(x,y)

# del users : it will delete the dictonary users

print(len(users))

# users.clear() it will clear the dictonary

# copying dict.
user1 = users.copy()
user2 = dict(users)

#Nested Dictionary
child3 = {
    "name" : "aman",
    "year" : "2001"
}
family = {
    "child1" : {
        "name": "Aditya",
        "Year": "2002"
    },
    "child2":{
        "name": "Aniket",
        "Year": "2000"
    },
    "child3":child3
}

for nesteditem in family.values():
    for x,y in nesteditem.items():
        print(x,y)

