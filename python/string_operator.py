string1 = "Aditya"
print(string1)
for i in string1:
    print(i)
print(string1[3])


# This is List
ls = ["orange","apple","banana"]
for i in ls:
    print(i)
print(ls)
print(ls[1])
print(ls[1][1])

print(string1 * 3)

day = "Friday"
print("Fri" in day) # true
print("fri" in day) #false
print("day" in day) #true
print("rida" in day) # true

# String replacement fields

weight = 50
print("My weight is " + str(weight) + " kgs")
print("My weight is {0} kgs".format(weight))
print("We have {0} days in {1}, {2}, {3}, {4}, {5}".format(31,"Jan","March","May","July","August"))
print("We have {0} days in {1}, {1}, {2}, {2}, {2}".format(31,"Jan","March"))

# String formatting
for i in range(1,11):
    print("No. {0} is squared is {1} and cubed is {2}".format(i,i**2,i**3))

for i in range(1,11):
    print("No. {0:2} is squared is {1:3} and cubed is {2:4}".format(i,i**2,i**3))
print()
# use < symbol for left allign and ^ symbol for middle align
for i in range(1,11):
    print("No. {0:<2} is squared is {1:<3} and cubed is {2:<4}".format(i,i**2,i**3))

#precision in python
print(22/7) # the default precision in python is 15

# if we use "f" the decimal have come 6 value after point
print("{0:10f}".format(22/7))
print("{0:.2f}".format(22/7))

#fstrings 
print(f"My weight is {weight} kgs")
print(f"the value of pi is {22/7:.2f}")
