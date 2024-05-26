class Citizen:

    def __init__(self,addhar_no):
        self.addhar_no = addhar_no

    def get_addhar(self):
        return self.addhar_no
    
class Person:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name
    
class Student(Person,Citizen):

    def __init__(self,name,roll_no,addhar_no):
        self.roll_no = roll_no

        Person.__init__(self,name)
        Citizen.__init__(self,addhar_no)

    def get_roll(self):
        return self.roll_no
    
s1 = Student("Aditya",4,123)

print("The name of the student is:",s1.get_name())
print("The roll no of the student is :", s1.get_roll())
print("The Addhar id of the student is :", s1.get_addhar())