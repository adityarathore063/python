from traceback import print_tb


age = int(input("Enter Your age"))

# And OR
# if age >= 18 and age <100: this is also right
if 18 <= age < 100 :
    print("You can vote")
else:
    print("Not eligble")

car = "BM"

if car=="BMW" or car == "Audi":
    print("Cool car")
else:
    print("Not cool")