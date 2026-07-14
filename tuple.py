#tuple are imutable

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

#accessing items by index
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 2
print(my_tuple[2])  # Output: 3
print(my_tuple[3])  # Output: 4
print(my_tuple[4])  # Output: 5

#lenghth of tuple
print(len(my_tuple))  # Output: 5

#nested tuple
tuple1 = (1, 2, (3, 4), 5)
tuple2 = (6, 7, 8)
nested_tuple = (tuple1, tuple2)
print(nested_tuple)

single_element_tuple = (1,)
print(single_element_tuple)  # Output: (1,)


#count  item in tupple specific item
my_tuple = (1, 2, 3,3 , 4, 5,)
print(my_tuple.count(3))  # Output: 2

letters_tuple = ('a', 'b', 'c', 'a', 'd')
print(letters_tuple.count('a'))  # Output: 2
print(letters_tuple.count('b'))  # Output: 1
print(letters_tuple.count('c'))  # Output: 1
print(letters_tuple.count('d'))  # Output: 1

print(letters_tuple.index('a'))  # Output: 0

#tuple unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30


person = ("Alice", 30, "New York")
name, age, city = person
print(name)  # Output: Alice
print(age)  # Output: 30
print(city)  # Output: New York
print(f"The person's name is {name}, age is {age}, and city is {city}.")

