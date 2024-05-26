str = "abcdef"
for val in str:
    print(val)
for i in range(10):
    print(i)
 # user input 
# for i in range(3):
#     val = input("Enter a number")
#     print(val)

# Truth value testing
a = False
if a == True:
    print("a is true")
else:
    print("a is false")

b = 1
if b == True:
    print("b is true")
else:
    print("b is false")

name = "Aditya"
if name:
    print("You have name")
else:
    print("You dont have name")

# in, not , casefold in python

letter = input("Enter the string")
if letter in name :
    print("Enter string is present in name")
else:
    print("Enter string is not present in name")
if letter not in name :
    print("Enter string is not present in name")
else:
    print("Enter string is present in name")


s = name.casefold() # it force to convert into smalllcase
print(s)

# iteration in range
for i in range(1,20):
    print("i is {0}".format(i))
for i in range(1,10):
    print("square of {0} is {1}".format(i,i**2))

for i in range(10,0,-1):
    print("square of {0} is {1}".format(i,i**2))

#Nested loops

for i in range(5):
    for j in range(5):
        print("* ",end="")
    print("\r")

# break and continue statement

for i in range(10):
    if i%2==0:
        continue
    else:
        print(i)

for i in range(10):
    if i==8:
        break
    else:
        print(i)

# while loop

num = int(input("Enter the number"))
k = 0

while k < num:
    print("k is {0}".format(k))
    k+=1