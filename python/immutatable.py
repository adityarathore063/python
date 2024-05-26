# Immutatable objects
# Int, float, bool, string, tuples, Frozen sets & byts

result = True
print(result)
print(id(result))

result = False
print(result)
print(id(result))

# Above are the example of immutatable object(cant change) , If you try to change the value contained in immutatable
# object so rather than the object updating its own value, a new ID/address is created for that new value and the
# immutatble object is unbinded from the previous ID and binding now with new id of value

