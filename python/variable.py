
a = 2
print(type(a))
b = 2.2
print(type(b))
str = "hello"
print(type(str))

str1,str2,str3 = "abc","xyz","def"
print(str1 +" " + str2 +" " + str3)
 #print(str1 +" " + str2 +" " + a) this gives error
 # strss = "hello",name = "aditya" this gives error

print(a+b) # float is the subclass of int but  str is not the subclass of int
 #print(a+str) it gives error because in backend isinstance() isSubclass() inbuilt function check then it give result
char = 'a'
print(type(char))
d = 0x69
print(d)
print(type(d))
# the binary prefix is 0b or 0B
#the octal prefix is 0o or 0O

print(0b10)
print(hex(0x69))

print("the string is " + hex(123)) # this is printing because hex function have return type str
print(type(hex(10)))

f = 1.2e3 # it moves decimal 3 places right and aaded 0 gives result 1200.0
print(f)

fr = 1.2
print(int(fr)) #type casting
# numeric data type
#int float complex
#float default show decimal precision upto 52 places
x = 5
y = 12
print(x+y)
print(y/x) # it gives float
print(y//x) # it gives int value
print(y%x)

#Followig are data type in python
# numeric
# iterators
# sequence(which are also iterators)
# Mapping
# files
# class
# exception