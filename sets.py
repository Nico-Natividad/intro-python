fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}


#no duplocate allowed in set
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

#check if an item is in a set
print("banana" in fruits)  # Output: True
print("orange" in fruits)  # Output: False

#adding items to a set
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

#not sure if item exist
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

#set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))  # Output: {4, 5}
print(set1.difference(set2))

#frozenet
locked_net = frozenset(['a','b','c'])
print(locked_net)
locked_net.add("d")


