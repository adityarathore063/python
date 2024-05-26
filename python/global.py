name = "aditya" #global variable

def func():
    name = "prince" # local variable
    print(name)

func()
print(name)

var = 4 #global variable

def func1():
    global var # here var becomes global variable and value also changes
    var = 5
    print(var)

print(var)
func1()
print(var)