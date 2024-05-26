# Mutatable object are those object whose value can be changed
# List, Dictionary,Set,Bytearray

grocery = ["bread","egg"]
# another_grocery = grocery
another_grocery = grocery.copy()

print(grocery)
print(id(grocery))

print()

print(another_grocery)
print(id(another_grocery))

print()

grocery+=["apple"]

print(grocery)
print(id(grocery))

print()

print(another_grocery) # it also print the apple for solving the mututability problem we can use copy function
print(id(another_grocery))
