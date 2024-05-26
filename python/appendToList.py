choice = "_"
grocery_items=[]

while choice!="0":
    if choice in "1234":
        print("Adding {0} big basket cart".format(choice))

        if choice=='1':
            grocery_items.append("butter")
        if choice=='2':
            grocery_items.append("bread")
        if choice=='3':
            grocery_items.append("milk")
        if choice=='4':
            grocery_items.append("tea bag")
    else:
        print("Add items from the following ones")
        print("1. butter")
        print("2. bread")
        print("3. milk")
        print("4. tea bag")
        print("0. Exit")
    choice = input(print("Enter your choice"))

    
print(grocery_items)