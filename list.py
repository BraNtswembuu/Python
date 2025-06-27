
fruits = ["banana", "apple", "orange", "mango"]
print(fruits[0])  # Accessing the first element

fruits[1] = "kiwi"  # Changing the second element
print(fruits)

fruits = ["banana", "kiwi", "orange", "mango"]  # Reassigning the list
fruits.append("grape")  # Adding a new element
print(fruits)

fruits.insert(2, "pear")  # Inserting an element at index 2
print(fruits)

fruits.remove("kiwi")  # Removing an element by value
print(fruits)

fruits.sort()  # Sorting the list
print(fruits)

fruits.reverse()  # Reversing the list
print(fruits)

fruits.pop()  # Removing the last element
print(fruits)