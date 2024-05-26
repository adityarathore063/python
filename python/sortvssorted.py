#sort does not return anything and it changes the existing values
#sorted it return the sorted list and it doesnot affect the existing list

num = [2,88,7,1,9,67]
another_num = sorted(num)

print(another_num)
print(num)


list1 = ["Aditya", "cat", "Dogaaa", "ca"]
list1.sort()
print(list1)

# for removing the uppercase and lowercase letter problem in sorting
list1.sort(key=str.casefold)
print(list1)

# for sorting in reverse order
list1.sort(key=str.casefold,reverse=True)
print(list1)

#for sorting with own function
def myFunc(e):
    return(len(e))
list1.sort(key=myFunc)
print(list1)