counter = 0

class Student:
    def __init__(self,roll_No, name):
        self.roll_No = roll_No
        self.name = name
    
    def print_values(self):
        print(self.roll_No)
        print(self.name)

def fetch_values():
    global counter
    counter+=1
    temp_name = input("Enter the name: ")

    return counter,temp_name

x,y = fetch_values()
s1 = Student(x,y)
x,y = fetch_values()
s2 = Student(x,y)

s1.print_values()
s2.print_values()