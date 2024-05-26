even = [2,4,6,8]
odd = [1,3,5,7]

even.extend(odd)
another_list = even
print(even)
print("This is another list")
print(another_list)
even.sort()

print(even)
print("This is another list")
print(another_list)
