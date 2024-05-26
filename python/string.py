
print("My name is Aditya Singh")

# This is comment

variable = "My name is :"
name = "Aditya Singh"

# namee = input("Enter your name : ")
# print(variable + " " + name)
# print(variable + " " + namee)

print('I am the "best"')

string1 = "Aditya"
print(string1[0])
print(string1[5])
print(string1[-1]) # it print from the last
print(string1[-3]) # print t
print(string1[1-4]) # print t


# Slicing in python
str1 = "Hello Aditya"
print(str1[0:4]) # slicing
print(str1[:7])
print(str1[8:])

print(str1[-5:-4])
# print(str1[-5:2]) this does not print anything because backward slicing is not possible
print(str1[-5:])

#step slicing 
print(str1[0:6:2]) # it skip 1 char. and print every 2nd character
num = "1,899,899,678,899,898"
print(num[1::4]) # print all comma

# backward slicing
print(str1[-5:0:-1])
print(str1[-5::-1])