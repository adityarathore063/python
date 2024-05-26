# def func():
#     print("This is function")

# def sum():
#     print("The sum of 5 and 7 is {}".format(5+7))
# func()
# sum()

# def name(first_name, last_name):
#     print(first_name,last_name)

# name("Aditya","Singh")

# using return
# def summ(a,b):
#     return a+b

# print(summ(7,8))


# passing multiple argument to single argument
# def func(*args):
#     print("The second member is "+ args[1])
#     for item in args:
#         print(item)

# func("aditya","aniket","prince")

# keyword argument (key , pair syntax)
# def func1(**kwargs): # we can also write (child1, child2, child3)
#     print(kwargs["child1"],kwargs["child2"],kwargs["child3"])

# func1(child2="aditya",child1="aniket",child3="prince")

# default argument
# def func2(first="aditya"):
#     print(first)

# func2()
# func2("aniket")

# passing list as argument

# def func3(fruit):
#     for item in fruit:
#         print(item)


# fruit = ["orange","apple","mango"]

# func3(fruit)

# list is mutuable
# int is immutable
# pass by value and reference

def func(var):
    var = 20

var = 10
func(var) # not change  the value of var
print(var)

def func1(arr):
    arr[0] = 0

def func2(arr):
    arr = [78,67]

arr = [18,89,90]


func1(arr) # it will change the array element value
print(arr)

func2(arr) # it will not affect the array value
print(arr)

# swapping 
def swap(a, b):
    #a,b = b,a or
    temp =a 
    a = b
    b = temp

    return a,b

a = 10
b = 20

a, b = swap(a,b)
print(a,b)

# easy way of swapping
x = 5
y = 4
x,y = y,x
print(x,y)







