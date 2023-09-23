# Abdullahi Suleiman
"""Create a grocery list containing at least 6 items
"""

# LISTS OF GROCERY
grocery_list = ["apples", "bread", "milk", "eggs", "chicken", "rice"]
print(grocery_list)

"""
Write a python program to print the indexes of the previously created list using the following index (index 2, 2 till end, 4 and 5)

"""
for var in iterable:
    statements
"""
for loop in a list
grocery_list = ["apples", "bread", "milk", "eggs", "chicken", "rice"] 
for goods in grocery_list:
    print(goods)
    # if goods == "eggs":
    i = goods
    print(i)
    if i == goods[3]:
        break

numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)


"""
Write a program to append, insert, extend, remove to the list
"""

# grocery list
grocery_list = ["apples", "bread", "milk", "eggs", "chicken", "rice"]

# Append an item to the end of the list
grocery_list.append("lettuce")
print("After appending 'lettuce':", grocery_list)

# Insert an item at a specific index (index 2)
grocery_list.insert(2, "cheese")
print("After inserting 'cheese' at index 2:", grocery_list)

# Extend the list with another list
additional_items = ["carrots", "orange juice"]
grocery_list.extend(additional_items)
print("After extending with 'carrots' and 'orange juice':", grocery_list)

# Remove an item by its value (e.g., remove 'chicken')
if "chicken" in grocery_list:
    grocery_list.remove("chicken")
print("After removing 'chicken':", grocery_list)

# Remove an item by its index (e.g., remove item at index 4)
if len(grocery_list) > 4:
    removed_item = grocery_list.pop(4)
    print(f"Removed item at index 4: {removed_item}")
print("After popping item at index 4:", grocery_list)


