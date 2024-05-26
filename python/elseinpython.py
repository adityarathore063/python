for i in range(1,5):
    print(i)
else:
    print("Executing else") # else is executed only when for loop is completed
print("After ending both for loop and else")

number = [1,3,5,7,9]

for i in number:
    if i%2==0:
        print("The number is unacceptable")
        break
else:
    print("The number is fine") # it executes only when above condition not satisifes