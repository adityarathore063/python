primeNo = {2,3,5,7}

# adding one item in set
primeNo.add(11)

# adding multiple items
primeNo.update([13,17,19])

# del primeNo it will delete the set
# primeNo.clear() it will clear the set items

# primeNo.pop() it will pop the last item so  it was  not useful because set is unotdered

# removing item from the set
primeNo.remove(5)
primeNo.discard(7)

for item in primeNo:
    print(item)

print(len(primeNo))

# union in set
even = {2,4,6,8}
odd = {1,3,5,7}

num = even.union(odd) # making the union
# even.update(odd) it will also make the union of set of even and odd
# print(even)
print(num)

num1 = {1,2,3,4,5}
num2 = {1,2,3,7,8}
num6 = {1,2}

num3 = num1.difference(num2) # num1.difference_update(num2) will also work as same
num4 = num2.difference(num1) # num2.difference_update(num1) will also work as same
print(num3)
print(num4)

num5 = num1.intersection(num2) # num1.intersection_update(num2) will also work as same
print(num5)

print(even.isdisjoint(odd)) # checking is disjoint set or not

print(num6.issubset(num1))

